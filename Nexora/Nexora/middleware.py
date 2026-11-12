
import zstandard as zstd

from django.utils.cache import patch_vary_headers


class ZstdResponseMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.compressor = zstd.ZstdCompressor(level=22)
        

    def accepts_zstd(self, request):

        accepted = request.headers.get("Accept-Encoding", "")

        for item in accepted.split(","):

            parts = item.strip().split(";")
            encoding = parts[0].strip().lower()

            quality = 1.0

            for parameter in parts[1:]:

                key, separator, value = parameter.strip().partition("=")

                if separator and key.strip().lower() == "q":

                    try:
                        quality = float(value.strip())
                    except ValueError:
                        quality = 0

            if encoding == "zstd" and 0 < quality <= 1:
                return True

            if encoding == "*" and 0 < quality <= 1:
                return True

        return False

    def __call__(self, request):
        
        response = self.get_response(request)

        # Only compress GET responses
        if request.method != "GET":
            return response

        # Check browser support
        if not self.accepts_zstd(request):
            return response

        # Check response eligibility
        if (
            response.status_code != 200
            or response.streaming
            or response.has_header("Content-Encoding")
            or response.has_header("Content-Range")
        ):
            return response

        # Respect no-transform
        cache_control = response.get("Cache-Control", "")

        if "no-transform" in [
            item.strip().lower()
            for item in cache_control.split(",")
        ]:
            return response

        # Check content type
        content_type = response.get("Content-Type", "").lower()

        compressible = (
            content_type.startswith("text/")
            or "application/json" in content_type
            or "+json" in content_type
            or "application/javascript" in content_type
            or "application/xml" in content_type
            or "+xml" in content_type
        )

        if not compressible:
            return response

        data = response.content

        # Skip small responses
        if len(data) < 1024:
            return response

        # Compress
        compressed = self.compressor.compress(data)

        # Avoid expanding the response
        if len(compressed) >= len(data):
            return response

        # Replace response body
        response.content = compressed

        # Update headers
        response["Content-Encoding"] = "zstd"
        response["Content-Length"] = str(len(compressed))

        # Preserve existing Vary values
        patch_vary_headers(response, ("Accept-Encoding",))

        # Remove invalidated representation metadata
        for header in ("ETag", "Content-MD5", "Digest", "Content-Digest"):
            if response.has_header(header):
                del response[header]

        return response




# import time
# import tracemalloc
# import zstandard as zstd

# from django.utils.cache import patch_vary_headers


# class ZstdResponseMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#         # Compression level
#         self.compression_level = 11

#         self.compressor = zstd.ZstdCompressor(
#             level=self.compression_level
#         )

#     def accepts_zstd(self, request):

#         accepted = request.headers.get("Accept-Encoding", "")

#         for item in accepted.split(","):

#             parts = item.strip().split(";")
#             encoding = parts[0].strip().lower()

#             quality = 1.0

#             for parameter in parts[1:]:

#                 key, separator, value = parameter.strip().partition("=")

#                 if separator and key.strip().lower() == "q":
#                     try:
#                         quality = float(value.strip())
#                     except ValueError:
#                         quality = 0

#             if encoding == "zstd" and 0 < quality <= 1:
#                 return True

#             if encoding == "*" and 0 < quality <= 1:
#                 return True

#         return False

#     def __call__(self, request):

#         response = self.get_response(request)

#         # Only compress GET requests
#         if request.method != "GET":
#             return response

#         if not self.accepts_zstd(request):
#             return response

#         # Skip ineligible responses
#         if (
#             response.status_code != 200
#             or response.streaming
#             or response.has_header("Content-Encoding")
#             or response.has_header("Content-Range")
#         ):
#             return response

#         # Respect no-transform
#         cache_control = response.get("Cache-Control", "")

#         if "no-transform" in [
#             item.strip().lower()
#             for item in cache_control.split(",")
#         ]:
#             return response

#         # Check content type
#         content_type = response.get("Content-Type", "").lower()

#         compressible = (
#             content_type.startswith("text/")
#             or "application/json" in content_type
#             or "+json" in content_type
#             or "application/javascript" in content_type
#             or "application/xml" in content_type
#             or "+xml" in content_type
#         )

#         if not compressible:
#             return response

#         data = response.content

#         old_size = len(data)

#         if old_size < 1024:
#             return response

#         # ==================================
#         # COMPRESSION PERFORMANCE MEASUREMENT
#         # ==================================

#         memory_tracking_started = False

#         if not tracemalloc.is_tracing():
#             tracemalloc.start()
#             memory_tracking_started = True

#         memory_before = tracemalloc.get_traced_memory()[0]

#         wall_start = time.perf_counter()
#         cpu_start = time.process_time()

#         compressed = self.compressor.compress(data)

#         cpu_end = time.process_time()
#         wall_end = time.perf_counter()

#         memory_current, memory_peak = tracemalloc.get_traced_memory()

#         if memory_tracking_started:
#             tracemalloc.stop()

#         # ==================================
#         # CALCULATE RESULTS
#         # ==================================

#         new_size = len(compressed)

#         saved_bytes = old_size - new_size

#         reduction = (saved_bytes / old_size) * 100

#         wall_time_ms = (wall_end - wall_start) * 1000
#         cpu_time_ms = (cpu_end - cpu_start) * 1000

#         memory_used = memory_peak - memory_before

#         # ==================================
#         # PRINT REPORT
#         # ==================================

#         print("\n========== ZSTANDARD PERFORMANCE REPORT ==========")

#         print(f"URL: {request.path}")
#         print(f"Compression level: {self.compression_level}")

#         print("\n--- SIZE ---")
#         print(f"Original:       {old_size:,} bytes")
#         print(f"Compressed:     {new_size:,} bytes")
#         print(f"Saved:          {saved_bytes:,} bytes")
#         print(f"Reduction:      {reduction:.2f}%")

#         print("\n--- TIME ---")
#         print(f"Wall time:      {wall_time_ms:.3f} ms")
#         print(f"CPU time:       {cpu_time_ms:.3f} ms")

#         print("\n--- MEMORY ---")
#         print(f"Peak increase:  {memory_used:,} bytes")
#         print(f"Current traced: {memory_current:,} bytes")

#         print("===================================================\n")

#         # Avoid expanding the response
#         if new_size >= old_size:
#             print("Compression skipped: output is not smaller.")
#             return response

#         # Replace response body
#         response.content = compressed

#         response["Content-Encoding"] = "zstd"
#         response["Content-Length"] = str(new_size)

#         patch_vary_headers(response, ("Accept-Encoding",))

#         # Remove invalidated representation metadata
#         for header in (
#             "ETag",
#             "Content-MD5",
#             "Digest",
#             "Content-Digest",
#         ):
#             if response.has_header(header):
#                 del response[header]

#         print("Zstandard compression applied successfully.")

#         return response

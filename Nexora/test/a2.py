
import zstandard as zstd
import time
import json
import random
import string
import statistics

# Generate approximately 3 MB of varied JSON data
random.seed(42)

records = []

while True:
    record = {
        "student_id": random.randint(100000, 999999),
        "name": "".join(random.choices(string.ascii_letters, k=12)),
        "email": "".join(random.choices(string.ascii_lowercase, k=10)) + "@example.com",
        "subject": random.choice([
            "Python", "Mathematics", "Physics",
            "Chemistry", "Data Science", "Business"
        ]),
        "score": round(random.uniform(10, 100), 2),
        "attendance": random.randint(0, 100),
        "description": "".join(
            random.choices(string.ascii_letters + " ", k=100)
        ),
        "active": random.choice([True, False])
    }

    records.append(record)

    data = json.dumps(records).encode("utf-8")

    if len(data) >= 3 * 1024 * 1024:
        break

original_size = len(data)

print(f"Original size: {original_size / (1024 * 1024):.2f} MB")

# Compression benchmark
levels = [3, 10, 11, 15, 19, 22]
runs = 5

print("\nZSTANDARD BENCHMARK\n")

for level in levels:

    compressor = zstd.ZstdCompressor(level=level)

    # Warm-up
    compressor.compress(data)

    times = []
    compressed = None

    for _ in range(runs):

        start = time.perf_counter()

        compressed = compressor.compress(data)

        end = time.perf_counter()

        times.append((end - start) * 1000)

    compressed_size = len(compressed)

    reduction = (
        (original_size - compressed_size) / original_size
    ) * 100

    print({
        "level": level,
        "original_bytes": original_size,
        "compressed_bytes": compressed_size,
        "saved_bytes": original_size - compressed_size,
        "reduction_percent": round(reduction, 2),
        "average_time_ms": round(statistics.mean(times), 3),
        "fastest_time_ms": round(min(times), 3),
        "slowest_time_ms": round(max(times), 3)
    })

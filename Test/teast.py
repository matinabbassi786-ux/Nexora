
import os
import base64
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# File paths
HERE = Path(__file__).resolve().parent
KEY_FILE = HERE / "nexora.key"
OUTPUT_FILE = HERE / "encrypted_data.txt"


def load_or_create_key():
    """Load the existing key or create one."""
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()

    key = AESGCM.generate_key(bit_length=256)
    KEY_FILE.write_bytes(key)

    try:
        os.chmod(KEY_FILE, 0o600)
    except OSError:
        pass

    return key


def encrypt_text(text):
    """Encrypt text using one AES-256-GCM layer."""
    key = load_or_create_key()
    aes = AESGCM(key)

    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        text.encode("utf-8"),
        None
    )

    # Save nonce and ciphertext together.
    encrypted_data = (
        base64.b64encode(nonce + ciphertext).decode("ascii")
    )

    OUTPUT_FILE.write_text(encrypted_data, encoding="utf-8")

    print("\nEncryption successful!")
    print("Algorithm: AES-256-GCM")
    print("Encryption layers: 1")
    print("Encrypted data:", encrypted_data)
    print("Saved to:", OUTPUT_FILE.name)


# def load_or_create_key():
#     """Load a valid AES-256 key or create one."""

#     if KEY_FILE.exists():
#         key = KEY_FILE.read_bytes()

#         # AES-256 requires exactly 32 bytes.
#         if len(key) == 32:
#             return key

#         print("Warning: Invalid key detected. Generating a new key.")

#     # Generate a valid 256-bit (32-byte) AES key.
#     key = AESGCM.generate_key(bit_length=256)

#     KEY_FILE.write_bytes(key)

#     try:
#         os.chmod(KEY_FILE, 0o600)
#     except OSError:
#         pass

#     return key



normal_text = input("Enter text to encrypt: ")
encrypt_text(normal_text)

key = KEY_FILE.read_bytes()
print("Encryption key:", key.hex())
# qkMxpehGFPs5HNUgbxRUp6Iti4Ekjqx3g0KhJeKHrPRiQX4=
# 8182e7c9b9d0246d76b7826a0bb838fc9431a8754e8d7ca73d4297d73d618af1
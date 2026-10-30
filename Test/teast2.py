import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def decode_encrypted_data():
    # Enter the saved encryption key in hexadecimal format.
    key_hex = input("Enter encryption key: ").strip()
    key = bytes.fromhex(key_hex)

    if len(key) != 32:
        print("Error: AES-256 requires a 32-byte key.")
        return

    # Enter the encrypted data (Base64).
    encrypted_data = input("Enter encrypted data: ").strip()

    try:
        raw_data = base64.b64decode(encrypted_data, validate=True)

        # First 12 bytes contain the nonce.
        nonce = raw_data[:12]
        ciphertext = raw_data[12:]

        # Decrypt using one AES-256-GCM layer.
        aes = AESGCM(key)
        plaintext = aes.decrypt(nonce, ciphertext, None)

        print("\nNormal text:", plaintext.decode("utf-8"))

    except Exception:
        print("Decryption failed: Check your encrypted data and key.")



decode_encrypted_data()

import os
import base64
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Use the SAME key created by your previous script.
KEY_FILE = Path("/home/matin/Desktop/Nexora/Test/nexora.key")

def encrypt_text(text):
    # Load the existing key.
    key = KEY_FILE.read_bytes()

    if len(key) != 32:
        raise ValueError("Invalid AES-256 key: expected 32 bytes.")

    # One encryption layer.
    aes = AESGCM(key)

    # Generate a fresh nonce for every encryption.
    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        text.encode("utf-8"),
        None
    )

    # Combine nonce and ciphertext for storage.
    encrypted_data = base64.b64encode(
        nonce + ciphertext
    ).decode("ascii")

    print("Encryption successful!")
    print("Encrypted data:", encrypted_data)

    return encrypted_data


# text = input("Enter text to encrypt: ")
# encrypt_text(text)

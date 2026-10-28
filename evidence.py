
import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


file_path = input("Enter the path of your evidence file: ").strip().strip('"')

if os.path.isfile(file_path):
    file_hash = calculate_hash(file_path)

    print("\n--- DIGITAL EVIDENCE REPORT ---")
    print("File Name:", os.path.basename(file_path))
    print("SHA-256 Hash:", file_hash)
else:
    print("Error: File not found. Check the file path.")

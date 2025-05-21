
import os
import hashlib

# Seznam známých "škodlivých" hashů (SHA-256)
known_viruses = {
    "5d41402abc4b2a76b9719d911017c592",  # "hello"
    "6b1b36cbb04b41490bfc0ab2bfa26f86"   # "test"
}

def hash_file(path):
    sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[ERROR] Cant read {path}: {e}")
        return None

def scan_directory(directory):
    print(f"\n📂 Checking Folder: {directory}")
    for root, _, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            print(f"🔍 Checking: {filepath}")
            file_hash = hash_file(filepath)
            if file_hash in known_viruses:
                print(f"⚠️ VIRTUS DETECTED!: {filepath}")
            else:
                print("✅ Clean")

if __name__ == "__main__":
    slozka = input("Insert path of folder you want to scan: ")
    if os.path.isdir(slozka):
        scan_directory(slozka)
    else:
        print("❌ Incorect Folder.")

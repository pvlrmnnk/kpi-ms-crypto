import hashlib

def hack_md5(hash):
    for i in range(100000):
        pin = f"{i:05d}"
        current_hash = hashlib.md5(pin.encode()).hexdigest()
        
        if current_hash == hash:
            return pin
            
    return None

if __name__ == "__main__":
    hash = "482c811da5d5b4bc6d497ffa98491e38" # password123
    pin = hack_md5(hash)
    print(f"Хеш: {hash}")
    print(f"Пін: {pin}")

    hash = hashlib.md5(b'12345').hexdigest()
    pin = hack_md5(hash)
    print(f"Хеш: {hash}")
    print(f"Пін: {pin}")

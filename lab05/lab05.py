import hashlib
import time

def hack_md5(hash, range_max):
    for i in range(range_max):
        pin = f"{i:05d}"
        current_hash = hashlib.md5(pin.encode()).hexdigest()
        
        if current_hash == hash:
            return pin
            
    return None

if __name__ == "__main__":

    hash = hashlib.md5(b'12345').hexdigest()
    start_time = time.time()
    start_time = time.time()
    pin = hack_md5(hash, 100000)
    elapsed_time = time.time() - start_time
    print(f"Хеш: {hash}")
    print(f"Затрачено часу на 100 000 варіантів: {int(elapsed_time)}c")
    print(f"Пін: {pin}")

    hash = "482c811da5d5b4bc6d497ffa98491e38" # password123
    start_time = time.time()
    pin = hack_md5(hash, 100000000)
    elapsed_time = time.time() - start_time
    print(f"Хеш: {hash}")
    print(f"Затрачено часу на 100 000 000 варіантів: {int(elapsed_time)}c")
    print(f"Пін: {pin}")


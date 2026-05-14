import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_aes_ctr(key, plaintext):
    # У режимі CTR використовується nonce довжиною 16 байт
    nonce = os.urandom(16)
    
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    
    return nonce, ciphertext

def decrypt_aes_ctr(key, nonce, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    return plaintext

if __name__ == "__main__":
    # Генеруємо випадковий 256-бітний ключ (32 байти). Варіанти: 16, 24, 32
    secret_key = os.urandom(32) 
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit".encode('utf-8')
    print(f"Оригінальний текст:  {text.decode('utf-8')}")
    print(f"Ключ:                {secret_key.hex()}")
    
    nonce, encrypted_text = encrypt_aes_ctr(secret_key, text)
    print(f"Згенерований nonce:  {nonce.hex()}")
    print(f"Зашифрований текст:  {encrypted_text.hex()}")
    
    decrypted_text = decrypt_aes_ctr(secret_key, nonce, encrypted_text)
    print(f"Розшифрований текст: {decrypted_text.decode('utf-8')}")
    
    assert text == decrypted_text, f"Щось пішло не так :-/"

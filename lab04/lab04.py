import itertools

def _apply_xor(data_bytes, key):
    """Внутрішня базова функція для XOR-операції."""
    key_bytes = key.encode('ascii')
    return bytes(d ^ k for d, k in zip(data_bytes, itertools.cycle(key_bytes)))

def encrypt_text_to_hex(clear_text, key):
    """Шифрує звичайний текст і повертає hex-рядок."""
    return _apply_xor(clear_text.encode('ascii'), key).hex()

def decrypt_hex_to_text(cipher_hex, key):
    """Дешифрує hex-рядок і повертає звичайний текст."""
    return _apply_xor(bytes.fromhex(cipher_hex), key).decode('ascii')

def apply_key_to_hex(cipher_hex, key):
    """Додає або знімає шар шифрування з hex-рядка (для проміжних кроків)."""
    return _apply_xor(bytes.fromhex(cipher_hex), key).hex()

def hack_xor(msg1_hex, msg2_hex, msg3_hex):
    """
    Зламує протокол, маючи три перехоплені hex-повідомлення.
    Виконує XOR між усіма трьома повідомленнями одночасно.
    """
    bytes1 = bytes.fromhex(msg1_hex)
    bytes2 = bytes.fromhex(msg2_hex)
    bytes3 = bytes.fromhex(msg3_hex)
    
    decrypted_bytes = bytes(b1 ^ b2 ^ b3 for b1, b2, b3 in zip(bytes1, bytes2, bytes3))
    
    return decrypted_bytes.decode('ascii')

if __name__ == "__main__":
    text = "Lorem ipsum dolor sit amet"
    key_alice = "alice_secret_key"
    key_bob = "bob_secret_key"

    print(f"Оригінальний текст:        {text}")

    msg1 = encrypt_text_to_hex(text, key_alice)
    print(f"Крок 1 (Аліса -> Боб):     {msg1}")

    msg2 = apply_key_to_hex(msg1, key_bob)
    print(f"Крок 2 (Боб -> Аліса):     {msg2}")

    msg3 = apply_key_to_hex(msg2, key_alice)
    print(f"Крок 3 (Аліса -> Боб):     {msg3}")

    derypted_text = decrypt_hex_to_text(msg3, key_bob)
    print(f"Крок 4 (Боб читає):        {derypted_text}")

    derypted_text = hack_xor(msg1, msg2, msg3)
    print(f"Розшифрований текст (хак): {derypted_text}")
def encode(text):
    """Перетворює в ASCII, потім у двійковий код, потім потроює кожен біт."""
    encoded_string = ""
    
    for char in text:
        binary_char = format(ord(char), '08b')
        for bit in binary_char:
            encoded_string += bit * 3
            
    return encoded_string


def decode(bits):
    """Виправляє помилки (по 3 біти), групує по 8 бітів і перетворює назад у текст."""
    corrected_bits = ""
    
    # Ітеруємо кожні 3 біти
    for i in range(0, len(bits), 3):
        triplet = bits[i:i+3]
        corrected_bits += '1' if triplet.count('1') > 1 else '0'
            
    decoded_text = ""
    
    # Ітеруємо кожні 8 біт
    for i in range(0, len(corrected_bits), 8):
        byte = corrected_bits[i:i+8]
        decoded_text += chr(int(byte, 2))
        
    return decoded_text

if __name__ == "__main__":
    text = "hey"
    print(f"Оригінальний текст: {text}")

    encoded = encode(text)
    print(f"Закодований текст:  {encoded}")
    
    corrupted_bits = "100111111000111001000010000111111000000111001111000111110110111000010111"
    print(f"Спотворений текст:  {corrupted_bits}")
    
    decoded = decode(corrupted_bits)
    print(f"Розкодований текст: {decoded}")

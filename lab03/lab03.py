def caesar(text, shift):
    decrypted_text = []
    
    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)
            
    return "".join(decrypted_text)

def caesar_bruteforce(encoded_message):
    freqs = {
        'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
        'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
        'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
        'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
        'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65, 'Z': 0.07
    }

    best_score = -1
    best_message = ""

    for shift in range(26):
        candidate_message = caesar(encoded_message, shift)
        
        score = 0
        for char in candidate_message:
            if char.isalpha():
                score += freqs[char.upper()]
                
        if score > best_score:
            best_score = score
            best_message = candidate_message

    return best_message

if __name__ == "__main__":

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    print("Оригінальний текст:")
    print(text)
    encrypted_text = caesar(text, 7)
    print("Зашифрований текст:")
    print(encrypted_text)
    derypted_text = caesar(encrypted_text, -7)
    print("Розшифрований текст:")
    print(derypted_text)
    derypted_text = caesar_bruteforce(encrypted_text)
    print("Розшифрований текст (брутфорс):")
    print(derypted_text)
    
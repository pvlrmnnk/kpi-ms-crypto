# Працюємо тільки з верхнім регістром
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def enigma_encrypt(text, start_shift, rotor1, rotor2, rotor3):
    def apply_shift(text):
        result = ""
        for i, char in enumerate(text):
            if char in ALPHABET:
                shift = start_shift + i
                new_idx = (ALPHABET.index(char) + shift) % len(ALPHABET)
                result += ALPHABET[new_idx]
            else:
                result += char
        return result

    def apply_rotor(text, rotor_mapping):
        result = ""
        for char in text:
            if char in ALPHABET:
                idx = ALPHABET.index(char)
                result += rotor_mapping[idx]
            else:
                result += char
        return result

    encrypted_text = apply_shift(text)
    encrypted_text = apply_rotor(encrypted_text, rotor1)
    encrypted_text = apply_rotor(encrypted_text, rotor2)
    encrypted_text = apply_rotor(encrypted_text, rotor3)
    
    return encrypted_text

def enigma_decrypt(text, start_shift, rotor1, rotor2, rotor3):
    def apply_reverse_shift(text):
        result = ""
        for i, char in enumerate(text):
            if char in ALPHABET:
                shift = start_shift + i
                old_idx = (ALPHABET.index(char) - shift) % len(ALPHABET)
                result += ALPHABET[old_idx]
            else:
                result += char
        return result

    def apply_reverse_rotor(text, rotor_mapping):
        result = ""
        for char in text:
            if char in ALPHABET:
                idx = rotor_mapping.index(char)
                result += ALPHABET[idx]
            else:
                result += char
        return result

    decrypted_text = apply_reverse_rotor(text, rotor3)
    decrypted_text = apply_reverse_rotor(decrypted_text, rotor2)
    decrypted_text = apply_reverse_rotor(decrypted_text, rotor1)
    decrypted_text = apply_reverse_shift(decrypted_text)

    return decrypted_text

if __name__ == "__main__":

    text = "AAA"
    expected_encrypted_text = "KQF"
    shift = 4
    r1 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    r2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    r3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    
    encrypted_text = enigma_encrypt(text, shift, r1, r2, r3)
    assert encrypted_text == expected_encrypted_text, f"Щось пішло не так :-/"
    decrypted_text = enigma_decrypt(encrypted_text, shift, r1, r2, r3)
    assert decrypted_text == text, f"Щось пішло не так :-/"
    print(f"Початкове повідомлення:    {text}")
    print(f"Зашифроване повідомлення:  {encrypted_text}")
    print(f"Розшифроване повідомлення: {decrypted_text}")

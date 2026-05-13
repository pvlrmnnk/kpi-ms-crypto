def caesar(text, shift):
    """
    Функція для зсуву тексту (шифрування або розшифрування) за методом Цезаря.
    Зсуває літери англійського алфавіту на задану кількість позицій.
    """
    decrypted_text = []
    
    for char in text:
        if char.isalpha() and char.isascii():
            # Визначаємо базовий код ASCII ('A' для великих літер, 'a' для малих)
            base = ord('A') if char.isupper() else ord('a')
            
            # Виконуємо зсув символу: 
            # 1. Знаходимо позицію літери в алфавіті (ord(char) - base)
            # 2. Віднімаємо зсув (- shift)
            # 3. Беремо остачу від ділення на 26, щоб не вийти за межі алфавіту (% 26)
            # 4. Повертаємося до кодів ASCII (+ base) та перетворюємо число назад у символ (chr)
            new_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)
            
    return "".join(decrypted_text)


def hack_caesar(encoded_message):
    """
    Функція для злому шифру Цезаря методом перебору (брутфорс).
    Використовує частотний аналіз англійської мови для пошуку правильного зсуву.
    """
    # Еталонні частоти літер в англійській мові (у відсотках)
    freqs = {
        'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
        'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
        'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
        'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
        'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65, 'Z': 0.07
    }

    best_score = -1
    best_message = ""

    # Перебираємо всі 26 можливих варіантів зсуву
    for shift in range(26):
        candidate_message = caesar(encoded_message, shift)
        
        score = 0
        
        # Аналізуємо кожен символ у поточному варіанті тексту
        for char in candidate_message:
            if char.isalpha():
                score += freqs[char.upper()]
                
        if score > best_score:
            best_score = score
            best_message = candidate_message

    return best_message


if __name__ == "__main__":
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    print(f"Оригінальний текст: {text}")
    
    encrypted_text = caesar(text, 7)
    print(f"Зашифрований текст: {encrypted_text}")
    
    derypted_text = caesar(encrypted_text, -7)
    print(f"Розшифрований текст: {derypted_text}")
    
    # Пробуємо зламати зашифрований текст без знання ключа за допомогою частотного аналізу
    derypted_text = hack_caesar(encrypted_text)
    print(f"Розшифрований текст (хак): {derypted_text}")

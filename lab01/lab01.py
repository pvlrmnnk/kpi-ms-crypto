import cv2
import numpy as np
import sys
import os

def get_permutation_table(seed, num_blocks):
    """Формує таблицю перестановок, використовуючи потік з LFSR"""

    def lfsr_generator():
        MASK = 0xFFFF
        state = seed & MASK

        while True:
            # Відводи (taps) для 16-бітної послідовності максимальної довжини 
            tap_16 = (state >> 15) & 1
            tap_14 = (state >> 13) & 1
            tap_13 = (state >> 12) & 1
            tap_11 = (state >> 10) & 1

            # Обчислення зворотного зв'язку  
            feedback_bit = tap_16 ^ tap_14 ^ tap_13 ^ tap_11

            # Зсув вліво
            state = ((state << 1) & MASK) | feedback_bit

            yield state

    rng_stream = lfsr_generator()
    indices = list(range(num_blocks))
    
    # Тасування Фішера-Єйтса
    for i in reversed(range(1, num_blocks)):
        lfsr_val = next(rng_stream)
        j = lfsr_val % (i + 1)
        indices[i], indices[j] = indices[j], indices[i]
        
    return indices

def encrypt_image(img, seed_key, grid):
    h, w, c = img.shape
    rows, cols = grid
    num_blocks = rows * cols
    
    bh = h // rows
    bw = w // cols
    
    # Обчислюємо точні розміри робочої області, відкидаємо залишок, якщо h/w не ділиться націло
    h_crop, w_crop = rows * bh, cols * bw
    working_img = img[:h_crop, :w_crop]
    
    # Отримуємо таблицю перестановок і конвертуємо в масив NumPy для індексації
    pt = np.array(get_permutation_table(seed_key, num_blocks))
    
    # Розбиваємо зображення на сітку блоків без циклів
    blocks = working_img.reshape(rows, bh, cols, bw, c)
    # Міняємо осі місцями, щоб згрупувати блоки
    blocks = blocks.swapaxes(1, 2)
    # Витягуємо в одновимірний список блоків
    blocks = blocks.reshape(num_blocks, bh, bw, c)
    
    # Шифрування
    encrypted_blocks = blocks[pt]
    
    # Збираємо блоки назад у зображення
    encrypted_img_crop = encrypted_blocks.reshape(rows, cols, bh, bw, c).swapaxes(1, 2).reshape(h_crop, w_crop, c)
    
    result = np.zeros_like(img)
    result[:h_crop, :w_crop] = encrypted_img_crop
    
    return result

def decrypt_image(img, seed_key, grid):
    h, w, c = img.shape
    rows, cols = grid
    num_blocks = rows * cols
    
    bh = h // rows
    bw = w // cols
    h_crop, w_crop = rows * bh, cols * bw
    working_img = img[:h_crop, :w_crop]
    
    pt = np.array(get_permutation_table(seed_key, num_blocks))
    
    # Розбиваємо на блоки аналогічним чином
    blocks = working_img.reshape(rows, bh, cols, bw, c).swapaxes(1, 2).reshape(num_blocks, bh, bw, c)
    
    # Для дешифрування розставляємо зашифровані блоки за оригінальними індексами
    decrypted_blocks = np.empty_like(blocks)
    decrypted_blocks[pt] = blocks
    
    # Збираємо зображення
    decrypted_img_crop = decrypted_blocks.reshape(rows, cols, bh, bw, c).swapaxes(1, 2).reshape(h_crop, w_crop, c)
    
    result = np.zeros_like(img)
    result[:h_crop, :w_crop] = decrypted_img_crop
    
    return result

if __name__ == "__main__":

    seed = 12345   
    grid = (16 * 3, 9 * 3) # зображення 16:9, тому сітка має бути кратною
    print(f"Сід:                     {seed}")

    root_dir = os.path.dirname(os.path.abspath(__file__))
    original_img_file = os.path.join(root_dir, "original.png")
    encrypted_img_file = os.path.join(root_dir, "encrypted.jpg")
    decrypted_img_file = os.path.join(root_dir, "decrypted.jpg")
    original_img = cv2.imread(original_img_file)

    encrypted_img = encrypt_image(original_img, seed, grid)
    cv2.imwrite(encrypted_img_file, encrypted_img)
    print(f"Зашифроване зображення:  {encrypted_img_file}")
    
    decrypted_img = decrypt_image(encrypted_img, seed, grid)
    cv2.imwrite(decrypted_img_file, decrypted_img)
    print(f"Розшифроване зображення: {decrypted_img_file}")

    
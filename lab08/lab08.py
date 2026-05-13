import math

def solve_discrete_log(g, h, q):
    """Знаходить найменше X таке, що g^X % q == h"""
    m = math.isqrt(q) + 1
    
    # Малі кроки
    # Обчислюємо g^j mod q для j від 0 до m-1
    # Зберігаємо у словнику {значення: показник}
    baby_steps = {}
    current_val = 1
    for j in range(m):
        if current_val not in baby_steps:
            baby_steps[current_val] = j
        current_val = (current_val * g) % q
    
    # Великі кроки
    # Обчислюємо h * (g^-m)^i mod q
    # g^-m — це зворотний елемент до g^m
    # Замість ділення, обчислимо фактор = g^-m mod q
    g_m = pow(g, m, q)
    try:
        # Використовуємо модульну інверсію для g^m
        factor = pow(g_m, -1, q)
    except ValueError:
        return None

    current_h = h
    for i in range(m):
        # Перевіряємо, чи є поточне значення в baby_steps
        if current_h in baby_steps:
            # Якщо h * (g^-m)^i = g^j, то g^(im + j) = h
            x = i * m + baby_steps[current_h]
            return x
        
        # Переходимо до наступного "кроку велетня"
        current_h = (current_h * factor) % q
        
    return None

if __name__ == "__main__":

    # https://www.codingame.com/ide/puzzle/discrete-log-problem
    tests = [
        {"g": 654, "h": 4547, "q": 11087, "expected_x": 114},
        {"g": 253941, "h": 1587010, "q": 2450219, "expected_x": 15331},
        {"g": 59930016, "h": 465179611, "q": 618142807, "expected_x": 36249002},
        {"g": 303566540, "h": 5272582361, "q": 11123061581, "expected_x": 100529399},
        {"g": 49999999961, "h": 42, "q": 49999999967, "expected_x": 23150749045},
        {"g": 42444879370, "h": 30224410788, "q": 49999999823, "expected_x": 49994563227}
    ]

    for i, t in enumerate(tests, 1):
        g, h, q, expected_x = t["g"], t["h"], t["q"], t["expected_x"]
        x = solve_discrete_log(g, h, q)
        assert x == expected_x, f"-Тест {i} expected_x={expected_x} x={x}"
        print(f"+Тест {i}: g={g} h={h} q={q} x={x}")

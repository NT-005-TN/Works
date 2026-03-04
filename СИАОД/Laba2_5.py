import time

# Обычный циклический подход
def power_iter(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Рекурсивный алгоритм (разделяй и властвуй)
def power_rec(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power_rec(base, exp // 2)
        return half * half
    else:
        return base * power_rec(base, exp - 1)

print("\n--- Задание 5: Возведение в степень ---")
b, e = 2, 20
print(f"{b}^{e} (Итеративно): {power_iter(b, e)}")
print(f"{b}^{e} (Рекурсивно): {power_rec(b, e)}")

# Замеры для большой степени
e_large = 10000
start = time.perf_counter()
power_iter(2, e_large)
t_iter = time.perf_counter() - start

start = time.perf_counter()
power_rec(2, e_large)
t_rec = time.perf_counter() - start

print(f"Время для степени {e_large}: Итеративно = {t_iter:.6f}, Рекурсивно = {t_rec:.6f}")
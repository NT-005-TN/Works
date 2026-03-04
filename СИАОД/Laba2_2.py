import time
import sys

# Рекурсивная реализация
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

# Циклическая реализация
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Замеры времени
n_values = [100, 500, 900]
print("\n--- Задание 2: Факториал ---")
for n in n_values:
    start = time.perf_counter()
    factorial_iter(n)
    time_iter = time.perf_counter() - start
    
    start = time.perf_counter()
    factorial_rec(n)
    time_rec = time.perf_counter() - start
    
    print(f"n={n}: Итеративно = {time_iter:.6f} сек, Рекурсивно = {time_rec:.6f} сек")

# Попытка вычислить factorial(1000) рекурсивно
print("\nПопытка вычисления factorial(1000) рекурсивно:")
try:
    # Увеличим лимит рекурсии для теста, если нужно, но по умолчанию будет ошибка
    # sys.setrecursionlimit(1500) 
    factorial_rec(1000)
    print("Успешно (лимит рекурсии был увеличен)")
except RecursionError as e:
    print(f"Ошибка: {e}")
    print("Причина: Превышена максимальная глубина стека вызовов (RecursionError).")

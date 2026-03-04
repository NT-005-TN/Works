import random

# 6.1 Декоратор memoize
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# 6.2 Число путей в прямоугольной сетке
@memoize
def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)

# 6.3 Умножение на случайную величину
def random_mult(n, depth=0, max_depth=5):
    if depth >= max_depth:
        return n
    coefficient = random.uniform(0.5, 2.0)
    return random_mult(n * coefficient, depth + 1, max_depth)

# 6.4 Проверка числа на простоту
def is_prime_rec(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_rec(n, divisor + 1)

print("\n--- Задание 6: Мемоизация ---")
print(f"Пути в сетке 10x10: {grid_paths(10, 10)}")
print(f"Случайное умножение 10: {random_mult(10)}")
print(f"17 простое? {is_prime_rec(17)}")
print(f"97 простое? {is_prime_rec(97)}")
import time
import random
import matplotlib.pyplot as plt

# Реализация пузырковой сортировки
def bubble_sort(arr):
    n = len(arr)
    # Копируем массив, чтобы не сортировать исходный повторно
    data = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

# Параметры эксперимента
sizes = [100, 200, 400, 800, 1600, 3200]
repeats = 5
times = []

print("Запуск экспериментов для пузырьковой сортировки...")

for n in sizes:
    total_time = 0
    for _ in range(repeats):
        # Генерируем случайный массив
        data = [random.randint(0, 10000) for _ in range(n)]
        
        start_time = time.perf_counter()
        bubble_sort(data)
        end_time = time.perf_counter()
        
        total_time += (end_time - start_time)
    
    avg_time = total_time / repeats
    times.append(avg_time)
    print(f"n={n}: Среднее время = {avg_time:.6f} сек")

# Построение графиков
plt.figure(figsize=(12, 5))

# График 1: Время от n
plt.subplot(1, 2, 1)
plt.plot(sizes, times, marker='o', label='Экспериментальные данные')
plt.title('Зависимость времени от n (Bubble Sort)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.grid(True)
plt.legend()

# График 2: Время от n^2 (для проверки линейности зависимости от квадрата)
# Если алгоритм O(n^2), то график t(n) от n^2 должен быть почти прямой линией
n_squared = [x**2 for x in sizes]
plt.subplot(1, 2, 2)
plt.plot(n_squared, times, marker='s', color='orange', label='t(n) от n^2')
plt.title('Зависимость времени от n^2')
plt.xlabel('n^2')
plt.ylabel('Время (сек)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

import time
import random
import matplotlib.pyplot as plt

# --- 1. Пузырьковая сортировка (O(n^2)) ---
def bubble_sort(arr):
    n = len(arr)
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

# --- 2. Ручная реализация алгоритма Timsort (O(n log n)) ---
# Он сочетает Insertion Sort (для мелких частей) и Merge Sort (для объединения)

RUN = 32  # Размер блока для сортировки вставками (стандартное значение в Python)

def insertion_sort(arr, left, right):
    """Сортировка вставками для небольшого отрезка массива"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    """Функция слияния двух отсортированных частей"""
    len1 = m - l + 1
    len2 = r - m
    left = arr[l : l + len1]
    right = arr[m + 1 : m + 1 + len2]

    i = 0
    j = 0
    k = l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timsort_manual(arr):
    """Ручная реализация логики Timsort"""
    data = arr.copy()
    n = len(data)
    
    # 1. Сортируем небольшие блоки через Insertion Sort
    for i in range(0, n, RUN):
        end = min(i + RUN - 1, n - 1)
        insertion_sort(data, i, end)
    
    # 2. Сливаем отсортированные блоки через Merge Sort
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:  # Если есть что сливать
                merge(data, left, mid, right)
        size = 2 * size
        
    return data

# --- Параметры эксперимента ---
sizes = [1000, 2000, 5000, 10000]
times_bubble = []
times_timsort = []

print("Запуск сравнения сортировок (ручная реализация)...")

for n in sizes:
    # --- Замер Bubble Sort ---
    data = [random.randint(0, 100000) for _ in range(n)]
    start = time.perf_counter()
    bubble_sort(data)
    times_bubble.append(time.perf_counter() - start)
    
    # --- Замер Manual Timsort ---
    data = [random.randint(0, 100000) for _ in range(n)]
    start = time.perf_counter()
    timsort_manual(data)
    times_timsort.append(time.perf_counter() - start)

    print(f"n={n}: Bubble={times_bubble[-1]:.4f}s, Manual Timsort={times_timsort[-1]:.5f}s")

# --- Построение графика ---
plt.figure(figsize=(10, 6))
plt.plot(sizes, times_bubble, marker='o', label='Bubble Sort O(n^2)', color='red', linewidth=2)
plt.plot(sizes, times_timsort, marker='s', label='Manual Timsort O(n log n)', color='green', linewidth=2)
plt.title('Сравнение производительности: Пузырьковая vs Ручная Timsort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время (сек)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
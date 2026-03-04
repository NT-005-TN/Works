import sys

# Чтение текста из файла
def read_text_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return ""

# Циклическая реализация
def count_spaces_iter(text):
    count = 0
    for char in text:
        if char == ' ':
            count += 1
    return count

# Рекурсивная реализация с обработкой частями
def count_spaces_rec(text, chunk_size=500):
    if not text:  # Терминальная часть
        return 0
    # Обрабатываем часть строки рекурсивно
    if len(text) <= chunk_size:
        if not text:
            return 0
        current = 1 if text[0] == ' ' else 0
        return current + count_spaces_rec(text[1:], chunk_size)
    else:
        # Разбиваем на части для избежания переполнения
        chunk = text[:chunk_size]
        rest = text[chunk_size:]
        return count_spaces_iter(chunk) + count_spaces_rec(rest, chunk_size)

# Загрузка текста из файла
text = read_text_from_file('Тестовый текст.txt')

print("\n--- Задание 3: Подсчет пробелов ---")
print(f"Длина текста: {len(text)} символов")
print(f"Цикл: {count_spaces_iter(text)}")
print(f"Рекурсия: {count_spaces_rec(text)}")
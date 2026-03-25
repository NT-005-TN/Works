def min_cost_path(grid):
    """
    Поиск минимальной стоимости пути в сетке с восстановлением маршрута
    Возвращает: минимальную стоимость, список координат пути
    """
    rows, cols = len(grid), len(grid[0])
    
    # Таблица ДП для стоимостей
    dp = [[0] * cols for _ in range(rows)]
    # Таблица для восстановления пути
    path = [[None] * cols for _ in range(rows)]
    
    # Инициализация начальной клетки
    dp[0][0] = grid[0][0]
    
    # Заполнение первой строки (можно прийти только слева)
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        path[0][j] = (0, j-1)
    
    # Заполнение первого столбца (можно прийти только сверху)
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        path[i][0] = (i-1, 0)
    
    # Заполнение остальной таблицы
    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i-1][j] < dp[i][j-1]:
                # Лучше прийти сверху
                dp[i][j] = dp[i-1][j] + grid[i][j]
                path[i][j] = (i-1, j)
            else:
                # Лучше прийти слева
                dp[i][j] = dp[i][j-1] + grid[i][j]
                path[i][j] = (i, j-1)
    
    # Восстановление пути обратным проходом
    route = []
    i, j = rows-1, cols-1
    while (i, j) != (0, 0):
        route.append((i, j))
        i, j = path[i][j]
    route.append((0, 0))
    route.reverse()
    
    return dp[rows-1][cols-1], route

# Генерация матрицы согласно заданию
grid = [[((i * 13 + j * 19 + 5) % 7) + 1 for j in range(128)] for i in range(128)]

# Добавление зон с повышенной стоимостью
for i in range(40, 90):
    for j in range(50, 55):
        grid[i][j] = 20

for i in range(70, 100):
    for j in range(80, 120):
        grid[i][j] = 15

# Выполнение алгоритма
min_cost, route = min_cost_path(grid)

# Вывод результатов
print("=" * 60)
print("ЗАДАНИЕ 4: Минимальная стоимость пути в сетке")
print("=" * 60)
print(f"Размер сетки: {len(grid)} × {len(grid[0])}")
print(f"Минимальная стоимость: {min_cost}")
print(f"Длина маршрута: {len(route)} клеток")
print(f"Начальная клетка: {route[0]}")
print(f"Конечная клетка: {route[-1]}")
print(f"Первые 10 координат: {route[:10]}")
print(f"Последние 10 координат: {route[-10:]}")
print("=" * 60)
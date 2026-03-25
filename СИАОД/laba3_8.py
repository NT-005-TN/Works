def three_knapsack(items, capacities):
    """
    Динамическое программирование для задачи о трёх рюкзаках
    Возвращает: максимальную стоимость, распределение по рюкзакам
    """
    c1, c2, c3 = capacities
    n = len(items)
    
    # dp[w1][w2][w3] = максимальная стоимость при весах w1, w2, w3
    dp = [[[0]*(c3+1) for _ in range(c2+1)] for _ in range(c1+1)]
    
    # Для восстановления решения
    choice = [[[[-1]*(c3+1) for _ in range(c2+1)] for _ in range(c1+1)] for _ in range(n+1)]
    
    for idx, (name, w, v) in enumerate(items):
        for w1 in range(c1, -1, -1):
            for w2 in range(c2, -1, -1):
                for w3 in range(c3, -1, -1):
                    # Не берём предмет
                    choice[idx+1][w1][w2][w3] = 0
                    
                    # В рюкзак 1
                    if w1 >= w:
                        val = dp[w1-w][w2][w3] + v
                        if val > dp[w1][w2][w3]:
                            dp[w1][w2][w3] = val
                            choice[idx+1][w1][w2][w3] = 1
                    
                    # В рюкзак 2
                    if w2 >= w:
                        val = dp[w1][w2-w][w3] + v
                        if val > dp[w1][w2][w3]:
                            dp[w1][w2][w3] = val
                            choice[idx+1][w1][w2][w3] = 2
                    
                    # В рюкзак 3
                    if w3 >= w:
                        val = dp[w1][w2][w3-w] + v
                        if val > dp[w1][w2][w3]:
                            dp[w1][w2][w3] = val
                            choice[idx+1][w1][w2][w3] = 3
    
    # Восстановление решения
    bag1, bag2, bag3 = [], [], []
    w1, w2, w3 = c1, c2, c3
    
    for idx in range(n, 0, -1):
        ch = choice[idx][w1][w2][w3]
        if ch == 1:
            bag1.append(items[idx-1])
            w1 -= items[idx-1][1]
        elif ch == 2:
            bag2.append(items[idx-1])
            w2 -= items[idx-1][1]
        elif ch == 3:
            bag3.append(items[idx-1])
            w3 -= items[idx-1][1]
    
    return dp[c1][c2][c3], bag1, bag2, bag3

# Чтение данных из treasures.txt
with open('treasures.txt', 'r', encoding='utf-8') as f:
    exec(f.read())  # Загружаем переменную items

capacities = [10, 14, 18]

# Выполнение алгоритма
max_value, bag1, bag2, bag3 = three_knapsack(items, capacities)

# Вывод результатов
print("=" * 60)
print("ЗАДАНИЕ 8: Кладоискатели — Задача о трёх рюкзаках")
print("=" * 60)
print(f"Всего предметов: {len(items)}")
print(f"Вместимость рюкзака Пети: {capacities[0]} кг")
print(f"Вместимость рюкзака Васи: {capacities[1]} кг")
print(f"Вместимость рюкзака Терентия: {capacities[2]} кг")
print(f"Максимальная стоимость: {max_value}")
print("-" * 60)
print(f"Рюкзак Пети: {len(bag1)} предметов, вес = {sum(i[1] for i in bag1)} кг")
for item in bag1[:5]:
    print(f"  - {item[0]} (вес: {item[1]}, стоимость: {item[2]})")
print("-" * 60)
print(f"Рюкзак Васи: {len(bag2)} предметов, вес = {sum(i[1] for i in bag2)} кг")
for item in bag2[:5]:
    print(f"  - {item[0]} (вес: {item[1]}, стоимость: {item[2]})")
print("-" * 60)
print(f"Рюкзак Терентия: {len(bag3)} предметов, вес = {sum(i[1] for i in bag3)} кг")
for item in bag3[:5]:
    print(f"  - {item[0]} (вес: {item[1]}, стоимость: {item[2]})")
print("=" * 60)
def greedy_change(amount, coins):
    """
    Жадный алгоритм: выбирает максимальный номинал на каждом шаге
    """
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return result if remaining == 0 else None

def dp_change(amount, coins):
    """
    Динамическое программирование: гарантирует минимальное количество купюр
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return None
    
    # Восстановление решения
    result = []
    current = amount
    while current > 0:
        result.append(parent[current])
        current -= parent[current]
    
    return result

# Данные из задания
coins1 = [1, 5, 10, 25, 50, 100]  # Стандартная система
coins2 = [1, 4, 6, 9]              # Нестандартная система
amounts = [23, 37, 58, 74, 99, 123]

# Выполнение и вывод результатов
print("=" * 70)
print("ЗАДАНИЕ 7: Размен монет — Сравнение жадного алгоритма и ДП")
print("=" * 70)
print(f"{'Сумма':<6} | {'Номиналы':<12} | {'Жадный':<8} | {'ДП':<6} | {'Совпадение':<10} | {'Жадный состав':<25}")
print("-" * 70)

for amt in amounts:
    for name, coins in [("Стандарт", coins1), ("Нестандарт", coins2)]:
        greedy = greedy_change(amt, coins)
        dp = dp_change(amt, coins)
        
        greedy_count = len(greedy) if greedy else None
        dp_count = len(dp) if dp else None
        match = greedy_count == dp_count if greedy and dp else False
        greedy_str = '+'.join(map(str, greedy)) if greedy else '-'
        
        print(f"{amt:<6} | {name:<12} | {greedy_count:<8} | {dp_count:<6} | {'Да' if match else 'Нет':<10} | {greedy_str:<25}")

print("=" * 70)
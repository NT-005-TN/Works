def lcs_with_table(a, b):
    """
    Поиск наибольшей общей подпоследовательности с таблицей ДП
    Возвращает: длину LCS, саму последовательность, таблицу ДП
    """
    m, n = len(a), len(b)
    
    # Создание таблицы ДП размером (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Заполнение таблицы
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                # Символы совпали — увеличиваем длину на 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Символы не совпали — берём максимум из двух вариантов
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Восстановление последовательности обратным проходом
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            # Символ входит в LCS
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            # Идём вверх
            i -= 1
        else:
            # Идём влево
            j -= 1
    
    lcs.reverse()  # Разворачиваем, так как собирали с конца
    return dp[m][n], ''.join(lcs), dp

# Строки из задания
a = "QWJXNTZLPMRAVKSDHUEYCIFOGBQRWPELKJHGFDSAMNBVCXZQWERTYUIOPLKJHGFDSAZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMTRXQPLMNSHADOWPROTOCOLDELTASEVENXK91REDNODEALPHAOMEGASIGMATRACEVECTORCYBERLATTICEPHANTOMKEYMIRRORCHAINQUANTUMDRIFTHELIXSIGNALCRYPTONOVAARCGRIDZETAFRAMEDELTAFORGESTELLARCODEXIONPATHWAYNEXUSLOCKSEQUENCEPRIMEGLYPHAXIOMLAYEROBSIDIANLINKVORTEXCHANNELSPECTRALCOREMATRIXFUSIONTHREADKRYPTOSPHEREZLQMWNXPTRAKVSHDUEYFICOGBLRAPQMTNZXCVWQPOIUYTREWQLKJHGFDSAMNBVCXZQWERT"
b = "MNBVCXZLKJHGFDSAPOIUYTREWQZXCVBNMASDFGHJKLQWERTYUIOPMNBVCXZLKJHGFDSAQWERTYUIOPZXCVBNMLKJHGFDSAPROTOCOLSHADOWDELTASEVENXK91REDNODEALPHAOMEGASIGMATRACEVECTORCYBERLATTICEPHANTOMKEYMIRRORCHAINQUANTUMDRIFTHELIXSIGNALCRYPTONOVAARCGRIDZETAFRAMEDELTAFORGESTELLARCODEXIONPATHWAYNEXUSLOCKSEQUENCEPRIMEGLYPHAXIOMLAYEROBSIDIANLINKVORTEXCHANNELSPECTRALCOREMATRIXFUSIONTHREADKRYPTOSPHEREPLKMIJNUHBYGVTFCRDXESZWAQOMNPLKJIHGFEDCBAVTREWQLZXCVBNMASDFGHJKQWERTYUIOPLKJHG"

# Выполнение алгоритма
length, sequence, dp_table = lcs_with_table(a, b)

# Вывод результатов
print("=" * 60)
print("ЗАДАНИЕ 3: Наибольшая общая подпоследовательность")
print("=" * 60)
print(f"Длина строки A: {len(a)} символов")
print(f"Длина строки B: {len(b)} символов")
print(f"Длина LCS: {length}")
print(f"Размер таблицы ДП: {len(dp_table)} x {len(dp_table[0])}")
print(f"Последовательность (первые 50 символов): {sequence[:50]}")
print(f"Последовательность (символы 50-100): {sequence[50:100]}")
print(f"Последовательность (последние 50 символов): {sequence[-50:]}")
print("=" * 60)
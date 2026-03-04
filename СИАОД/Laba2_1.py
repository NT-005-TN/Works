from decimal import Decimal, getcontext
from fractions import Fraction

# Установка точности для Decimal
getcontext().prec = 50

# Исходные данные
prices_float = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

# 1. Расчет с использованием float
total_float = sum(prices_float)
discount_float = total_float * 0.93  # Скидка 7%
vat_float = discount_float * 1.20    # НДС 20%
part_float = vat_float / 3

# 2. Расчет с использованием Decimal (инициализация через строку для точности)
prices_decimal = [Decimal(str(p)) for p in prices_float]
total_decimal = sum(prices_decimal)
discount_decimal = total_decimal * Decimal('0.93')
vat_decimal = discount_decimal * Decimal('1.20')
part_decimal = vat_decimal / Decimal('3')

# 3. Расчет с использованием Fraction 
prices_fraction = [Fraction(str(p)) for p in prices_float]
total_fraction = sum(prices_fraction)
discount_fraction = total_fraction * Fraction(93, 100)  
vat_fraction = discount_fraction * Fraction(120, 100)   
part_fraction = vat_fraction / 3

# Вывод результатов
print("--- Задание 1: Сравнение типов данных ---")
print(f"Float:    Итоговая сумма = {vat_float:.10f}, Часть = {part_float:.10f}")
print(f"Decimal:  Итоговая сумма = {vat_decimal}, Часть = {part_decimal}")
print(f"Fraction: Итоговая сумма = {vat_fraction}, Часть = {part_fraction}")
from decimal import Decimal, getcontext
from fractions import Fraction

# Исходные данные
prices_float = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

# 1. Float
total_float = sum(prices_float)
discount_float = total_float * 0.93  # Скидка 7%
vat_float = discount_float * 1.20    # НДС 20%
part_float = vat_float / 3

# 2. Decimal (высокая точность)
getcontext().prec = 28
prices_dec = [Decimal(str(p)) for p in prices_float]
total_dec = sum(prices_dec)
discount_dec = total_dec * Decimal('0.93')
vat_dec = discount_dec * Decimal('1.20')
part_dec = vat_dec / Decimal('3')

# 3. Fraction (точное рациональное)
prices_frac = [Fraction(str(p)) for p in prices_float]
total_frac = sum(prices_frac)
discount_frac = total_frac * Fraction(93, 100)  
vat_frac = discount_frac * Fraction(120, 100)  
part_frac = vat_frac / 3

print(f"Float:    Итого {part_float:.10f}")
print(f"Decimal:  Итого {part_dec}")
print(f"Fraction: Итого {float(part_frac):.10f}")
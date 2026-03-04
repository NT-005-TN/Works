base_list = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]],[11,12,[13,[14,[15,[16,[17,[18]]]]]]],19,[20,[21,[22,[23,[24,[25,[26,[27,[28]]]]]]]]],29,[[30,[31,[32,[33,[34]]]]],35],36,[37,[38,[39,[40,[41,[42,[43]]]]]]],44,[45,[46,[47,[48,[49,[50,[51]]]]]]],52,[53,[54,[55,[56,[57,[58,[59,[60]]]]]]]],61,[[62],[[63,[64,[65]]]]],66,[67,[68,[69,[70,[71,[72,[73,[74]]]]]]]],75,[76,[77,[78,[79,[80,[81,[82]]]]]]],83,[84,[85,[86,[87,[88,[89,[90,[91]]]]]]]],92,[[93,[94,[95]]],96],97,[98,[99,[100]]]]

# Рекурсивная реализация
def flatten_rec(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_rec(item))
        else:
            flat.append(item)
    return flat

# Циклическая реализация (с использованием стека)
def flatten_iter(nested_list):
    stack = [nested_list]
    flat = []
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            flat.append(current)
    return flat

print("\n--- Задание 4: Развертывание списка ---")
res_rec = flatten_rec(base_list)
res_iter = flatten_iter(base_list)
print(f"Длина списка: {len(res_rec)}")
print(f"Совпадение результатов: {res_rec == res_iter}")
print(f"Первые 10 элементов: {res_rec[:10]}")
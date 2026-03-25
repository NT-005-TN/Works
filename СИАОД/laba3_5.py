# Чтение данных из файла works.txt
with open('works.txt', 'r', encoding='utf-8') as f:
    exec(f.read())  # Загружаем переменную events

def schedule_events(events):
    """Жадный алгоритм: выбор по минимальному времени окончания"""
    sorted_events = sorted(events, key=lambda x: (x[2], x[3]))  # сортировка по (день, конец)
    selected = []
    last_end = {}
    
    for event in sorted_events:
        name, day, start, end, desc = event
        start_min = start[0] * 60 + start[1]
        end_min = end[0] * 60 + end[1]
        
        if day not in last_end or start_min >= last_end[day]:
            selected.append(event)
            last_end[day] = end_min
    return selected

selected = schedule_events(events)
print(f"Всего мероприятий: {len(events)}")
print(f"Выбрано: {len(selected)}")
for evt in selected[:10]:
    print(f"{evt[1]} {evt[2]}-{evt[3]} | {evt[0]}")
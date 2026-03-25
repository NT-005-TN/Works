def min_refuel_stops(stations, total_distance, tank_capacity):
    """
    Жадный алгоритм: на каждом шаге выбираем самую дальнюю достижимую заправку
    Возвращает: количество остановок, список заправок, статус
    """
    stops = []
    current_position = 0
    
    # Добавляем конечную точку как финальную "заправку"
    all_points = stations + [total_distance]
    
    while current_position < total_distance:
        max_reachable = current_position + tank_capacity
        next_stop = None
        
        # Находим самую дальнюю заправку в пределах досягаемости
        for station in all_points:
            if current_position < station <= max_reachable:
                next_stop = station
        
        # Если ничего не нашли — маршрут невозможен
        if next_stop is None:
            return None, [], "Невозможно добраться до пункта назначения"
        
        # Если достигли финиша — завершаем
        if next_stop == total_distance:
            break
        
        stops.append(next_stop)
        current_position = next_stop
    
    return len(stops), stops, "Успешно"

# Данные из задания
stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 2010, 2170, 2330, 2480, 
            2650, 2810, 2970, 3140, 3300, 3460, 3630, 3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 
            5100, 5260, 5420, 5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 7380, 
            7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 9180, 9340, 9510, 9670, 9830, 
            10000, 10160, 10320]

total_distance = 10451
tank_capacity = 500

# Выполнение алгоритма
num_stops, stop_list, status = min_refuel_stops(stations, total_distance, tank_capacity)

# Вывод результатов
print("=" * 60)
print("ЗАДАНИЕ 6: Поездка до Владивостока")
print("=" * 60)
print(f"Статус: {status}")
print(f"Общая дистанция: {total_distance} км")
print(f"Вместимость бака: {tank_capacity} км")
print(f"Количество остановок: {num_stops}")
print(f"Первые 10 заправок: {stop_list[:10]}")
print(f"Последние 5 заправок: {stop_list[-5:]}")
print(f"Среднее расстояние между заправками: {total_distance/(num_stops+1):.1f} км")
print("=" * 60)
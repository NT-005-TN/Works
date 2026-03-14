"""
Модуль форматирования вывода
"""
from typing import List, Tuple, Optional
from constants import (
    EMOJI_PRIORITY, EMOJI_LATE, EMOJI_ADDED,
    EMOJI_ACTIVE, EMOJI_INACTIVE
)
from database import get_student_name


def get_student_prefix(is_priority: int, is_late: int, is_added: int) -> str:
    """
    Возвращает emoji-префикс для студента
    
    Args:
        is_priority: флаг приоритета
        is_late: флаг опоздания
        is_added: флаг добавленного
        
    Returns:
        Строка с emoji
    """
    if is_priority:
        return f"{EMOJI_PRIORITY} "
    if is_late:
        return f"{EMOJI_LATE} "
    if is_added:
        return f"{EMOJI_ADDED} "
    return ""


def format_queue_display(queue_id: int, subject: str, created_at: str,
                         updated_at: str, change_log: str, items: List[Tuple]) -> str:
    """
    Форматирует полную информацию об очереди для отображения
    
    Args:
        queue_id: ID очереди
        subject: предмет
        created_at: дата создания
        updated_at: дата обновления
        change_log: лог изменений
        items: элементы очереди
        
    Returns:
        Отформатированная строка
    """
    lines = [f"Очередь {subject}", f"Создана {created_at}"]
    
    # Показываем "Изменена" только если очередь реально менялась
    if (str(updated_at) != str(created_at)) or not (change_log and change_log.startswith("Создана")):
        lines.append(f"Изменена {updated_at} ({change_log})")
    lines.append("")
    
    for item in items:
        pos, sid, is_p, is_l, w_before, w_after, is_added = item
        prefix = get_student_prefix(is_p, is_l, is_added)
        name = get_student_name(sid)
        weight = w_after if w_after is not None else w_before
        lines.append(f"{pos}. {prefix}{name} — {weight:.2f}")
    
    return "\n".join(lines)


def format_queue_short(queue_id: int, subject: str, created_at: str) -> str:
    """
    Форматирует краткую информацию об очереди для списка
    
    Args:
        queue_id: ID очереди
        subject: предмет
        created_at: дата создания
        
    Returns:
        Краткая строка
    """
    return f"{created_at} — {subject}"


def format_student_list(students: List[Tuple]) -> str:
    """
    Форматирует список студентов
    
    Args:
        students: список кортежей (id, name, active)
        
    Returns:
        Отформатированная строка
    """
    lines = ["📝 <b>Список:</b>"]
    for s_id, name, active in students:
        status = EMOJI_ACTIVE if active else EMOJI_INACTIVE
        lines.append(f"<code>{s_id}</code>: {name} {status}")
    return "\n".join(lines)


def format_weights_list(students: List[Tuple]) -> str:
    """
    Форматирует список весов
    
    Args:
        students: список кортежей (name, weight)
        
    Returns:
        Отформатированная строка
    """
    lines = ["📊 <b>Веса:</b>"]
    for name, weight in students:
        lines.append(f"{name}: <code>{weight:.2f}</code>")
    return "\n".join(lines)


def format_weight_history(student_id: int, history: List[Tuple], max_entries: int = 10) -> str:
    """
    Форматирует историю весов студента
    
    Args:
        student_id: ID студента
        history: история изменений
        max_entries: максимальное количество записей
        
    Returns:
        Отформатированная строка
    """
    if not history:
        return "⚠️ Нет истории для этого студента"
    
    # Разворачиваем в хронологическом порядке
    history_chrono = list(reversed(history))
    lines = [f"📈 <b>История весов студента {student_id}</b>"]
    
    # Если только одна запись
    if len(history_chrono) == 1:
        w, ts, place = history_chrono[-1]
        place_txt = f" [{place}]" if place else ""
        lines.append(f"{ts}: {w:.2f}{place_txt}")
        return "\n".join(lines)
    
    # Формируем переходы prev -> cur
    for i in range(1, len(history_chrono)):
        prev_w, _, _ = history_chrono[i-1]
        cur_w, cur_ts, place = history_chrono[i]
        place_txt = f" [{place}]" if place else ""
        lines.append(f"{cur_ts}: {prev_w:.2f} → {cur_w:.2f}{place_txt}")
    
    # Возвращаем последние max_entries записей
    return "\n".join(lines[-max_entries:])

"""
Модуль валидации данных
"""
from typing import Optional, Tuple


def validate_positions(pos1: int, pos2: int) -> Tuple[bool, Optional[str]]:
    """
    Проверяет корректность позиций для обмена.
    
    Args:
        pos1: первая позиция
        pos2: вторая позиция
        
    Returns:
        Кортеж (успешно, сообщение об ошибке)
    """
    if pos1 <= 0 or pos2 <= 0:
        return False, "Позиции должны быть положительными числами"
    
    if pos1 == pos2:
        return False, "Выберите разные позиции"
    
    return True, None


def validate_queue_id(queue_id: Optional[int]) -> Tuple[bool, Optional[str]]:
    """
    Проверяет корректность ID очереди.
    
    Args:
        queue_id: ID очереди
        
    Returns:
        Кортеж (успешно, сообщение об ошибке)
    """
    if queue_id is None or queue_id <= 0:
        return False, "Неверный ID очереди"
    
    return True, None


def validate_student_id(student_id: Optional[int]) -> Tuple[bool, Optional[str]]:
    """
    Проверяет корректность ID студента.
    
    Args:
        student_id: ID студента
        
    Returns:
        Кортеж (успешно, сообщение об ошибке)
    """
    if student_id is None or student_id <= 0:
        return False, "Неверный ID студента"
    
    return True, None


def validate_subject(subject: str) -> Tuple[bool, Optional[str]]:
    """
    Проверяет корректность названия предмета.
    
    Args:
        subject: название предмета
        
    Returns:
        Кортеж (успешно, сообщение об ошибке)
    """
    if not subject or not subject.strip():
        return False, "Название предмета не может быть пустым"
    
    if len(subject.strip()) > 100:
        return False, "Название предмета слишком длинное (макс. 100 символов)"
    
    return True, None
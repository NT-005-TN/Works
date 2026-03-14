
"""
Состояния FSM для бота
"""
from aiogram.fsm.state import State, StatesGroup


class AdminStates(StatesGroup):
    """Состояния для админских операций"""
    awaiting_subject = State()  # Ожидание названия предмета
    awaiting_swap_positions = State()  # Ожидание позиций для обмена


class SelectionStates(StatesGroup):
    """Состояния для выбора элементов"""
    selecting_priority = State()
    selecting_late = State()
    selecting_enable = State()
    selecting_disable = State()
    selecting_swap = State()
    selecting_admin_add = State()
    selecting_admin_del = State()
"""
Утилиты приложения
"""
from .keyboards import (
    get_main_keyboard,
    get_selection_keyboard,
    get_swap_keyboard,
    get_admin_action_keyboard,
    get_student_selection_keyboard
)
from .formatters import (
    format_queue_display,
    format_student_list,
    format_weights_list,
    format_weight_history,
    get_student_prefix,
    format_queue_short
)

__all__ = [
    "get_main_keyboard",
    "get_selection_keyboard",
    "get_swap_keyboard",
    "get_admin_action_keyboard",
    "get_student_selection_keyboard",
    "format_queue_display",
    "format_student_list",
    "format_weights_list",
    "format_weight_history",
    "get_student_prefix",
    "format_queue_short"
]
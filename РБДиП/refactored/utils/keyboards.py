"""
Модуль генерации клавиатур
"""
from typing import Optional, List, Dict, Any
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants import (
    KEYBOARD_COLS, EMOJI_PRIORITY, EMOJI_LATE,
    EMOJI_ACTIVE, EMOJI_INACTIVE
)
from config import ADMINS
from database import get_student_name, get_queue, get_full_list, get_recent_queues


def is_admin(user_id: int) -> bool:
    """Проверяет, является ли пользователь админом"""
    return user_id in ADMINS


def get_main_keyboard(user_id: int, queue_id: Optional[int] = None) -> InlineKeyboardMarkup:
    """
    Генерирует основную клавиатуру
    
    Args:
        user_id: ID пользователя
        queue_id: ID текущей очереди (опционально)
        
    Returns:
        InlineKeyboardMarkup
    """
    buttons: List[List[InlineKeyboardButton]] = []
    
    if is_admin(user_id):
        # Админские кнопки
        buttons.append([InlineKeyboardButton(text="🎲 Сгенерировать", callback_data="admin_gen")])
        
        if queue_id:
            buttons.append([InlineKeyboardButton(text="🔀 Поменять местами", 
                                               callback_data=f"admin_swap_start_{queue_id}")])
            
            buttons.append([
                InlineKeyboardButton(text="⭐ Приоритеты", callback_data="sel_priority"),
                InlineKeyboardButton(text="🐌 Опоздания", callback_data="sel_late")
            ])
            
            buttons.append([
                InlineKeyboardButton(text="✅ Включить", callback_data="sel_enable"),
                InlineKeyboardButton(text="❌ Исключить", callback_data="sel_disable")
            ])
            
            buttons.append([
                InlineKeyboardButton(text="📌 Текущая очередь", callback_data="open_latest_queue"),
                InlineKeyboardButton(text="📜 Очереди", callback_data="pub_queues")
            ])
            
            buttons.append([
                InlineKeyboardButton(text="➕ Добавить студента", callback_data=f"admin_add_{queue_id}"),
                InlineKeyboardButton(text="➖ Удалить студента", callback_data=f"admin_del_{queue_id}")
            ])
        else:
            buttons.append([
                InlineKeyboardButton(text="📌 Текущая очередь", callback_data="open_latest_queue"),
                InlineKeyboardButton(text="📜 Очереди", callback_data="pub_queues")
            ])
        
        buttons.append([
            InlineKeyboardButton(text="📝 Список", callback_data="pub_list"),
            InlineKeyboardButton(text="📊 Веса", callback_data="pub_weights")
        ])
        
        buttons.append([InlineKeyboardButton(text="🔄 Включить всех", callback_data="admin_enable_all")])
        buttons.append([InlineKeyboardButton(text="📈 История весов", callback_data="pub_weight_history")])
    else:
        # Кнопки для обычных пользователей
        buttons.append([
            InlineKeyboardButton(text="📌 Текущая очередь", callback_data="open_latest_queue"),
            InlineKeyboardButton(text="📜 Очереди", callback_data="pub_queues")
        ])
        buttons.append([
            InlineKeyboardButton(text="📝 Список ID", callback_data="pub_list"),
            InlineKeyboardButton(text="📊 Шансы", callback_data="pub_weights")
        ])
        buttons.append([InlineKeyboardButton(text="📈 История весов", callback_data="pub_weight_history")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_selection_keyboard(user_id: int, selection_data: Dict[str, Any]) -> Optional[InlineKeyboardMarkup]:
    """
    Генерирует клавиатуру для выбора
    
    Args:
        user_id: ID пользователя
        selection_data: данные выбора
        
    Returns:
        InlineKeyboardMarkup или None
    """
    if not selection_data:
        return None
    
    action = selection_data.get("action")
    temp_selected = selection_data.get("selected", [])
    
    if action == "swap":
        return _get_swap_keyboard(selection_data, temp_selected)
    elif action in ("admin_add", "admin_del"):
        return _get_admin_action_keyboard(selection_data, temp_selected)
    else:
        return _get_general_selection_keyboard(selection_data, temp_selected)


def _get_swap_keyboard(selection_data: Dict, temp_selected: List[int]) -> InlineKeyboardMarkup:
    """Клавиатура для выбора обмена местами"""
    queue_id = selection_data.get("queue_id")
    queue = get_queue(queue_id) if queue_id else None
    
    if not queue:
        recent = get_recent_queues(1)
        if not recent:
            return InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text="⚠️ Нет очередей", callback_data="cancel_selection")
            ]])
        queue = get_queue(recent[0][0])
    
    buttons: List[List[InlineKeyboardButton]] = []
    row: List[InlineKeyboardButton] = []
    
    for item in queue["items"]:
        pos, sid, is_p, is_l, w_before, w_after, is_added = item
        
        # Пропускаем приоритетных, опоздавших и добавленных
        if is_p or is_l or is_added:
            continue
        
        prefix = "⭐ " if is_p else "🐌 " if is_l else "😭 " if is_added else ""
        check = "✅ " if pos in temp_selected else ""
        name = get_student_name(sid)
        
        row.append(InlineKeyboardButton(
            text=f"{check}{pos}. {prefix}{name}",
            callback_data=f"swap_toggle_{pos}"
        ))
        
        if len(row) == KEYBOARD_COLS:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    confirm_text = "🚀 ПОМЕНЯТЬ" if len(temp_selected) == 2 else "Выбери двоих"
    buttons.append([InlineKeyboardButton(text=confirm_text, callback_data="confirm_swap")])
    buttons.append([InlineKeyboardButton(text="🚫 Отмена", callback_data="cancel_selection")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def _get_admin_action_keyboard(selection_data: Dict, temp_selected: List[int]) -> InlineKeyboardMarkup:
    """Клавиатура для админских действий (добавление/удаление)"""
    queue_id = selection_data.get("queue_id")
    action = selection_data.get("action")
    
    if queue_id is None:
        return InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="⚠️ Нет очереди", callback_data="cancel_selection")
        ]])
    
    buttons: List[List[InlineKeyboardButton]] = []
    row: List[InlineKeyboardButton] = []
    
    if action == "admin_del":
        queue = get_queue(queue_id)
        for item in queue["items"]:
            pos, sid, is_p, is_l, w_before, w_after, is_added = item
            name = get_student_name(sid)
            check = "✅ " if pos in temp_selected else ""
            label = f"{check}{pos}. {name} {'⭐' if is_p else '🐌' if is_l else ''}"
            
            row.append(InlineKeyboardButton(
                text=label,
                callback_data=f"admin_del_toggle_{queue_id}_{pos}"
            ))
            
            if len(row) == KEYBOARD_COLS:
                buttons.append(row)
                row = []
    else:  # admin_add
        students = get_full_list()
        queue = get_queue(queue_id)
        present_ids = {item[1] for item in queue["items"]}
        
        for s_id, name, active in students:
            if s_id in present_ids:
                continue
            
            check = "✅ " if s_id in temp_selected else ""
            row.append(InlineKeyboardButton(
                text=f"{check}{name}",
                callback_data=f"admin_add_toggle_{queue_id}_{s_id}"
            ))
            
            if len(row) == KEYBOARD_COLS:
                buttons.append(row)
                row = []
    
    if row:
        buttons.append(row)
    
    # Кнопки подтверждения
    if action == "admin_add":
        buttons.append([InlineKeyboardButton(text="🚀 ДОБАВИТЬ", callback_data="admin_confirm_add")])
    else:
        buttons.append([InlineKeyboardButton(text="🚀 УДАЛИТЬ", callback_data="admin_confirm_del")])
    
    buttons.append([InlineKeyboardButton(text="🧹 Сбросить выбор", callback_data="clear_current_list")])
    buttons.append([InlineKeyboardButton(text="🚫 Отмена", callback_data="cancel_selection")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def _get_general_selection_keyboard(selection_data: Dict, temp_selected: List[int]) -> InlineKeyboardMarkup:
    """Клавиатура для общего выбора (приоритеты, опоздания, включение/выключение)"""
    action = selection_data.get("action")
    students = get_full_list()
    
    buttons: List[List[InlineKeyboardButton]] = []
    row: List[InlineKeyboardButton] = []
    
    for s_id, name, active in students:
        # Определяем префикс
        prefix = ""
        if action == "priority" and s_id in temp_selected:
            prefix = "⭐ "
        elif action == "late" and s_id in temp_selected:
            prefix = "🐌 "
        
        check = "✅ " if s_id in temp_selected else ""
        status_dot = EMOJI_ACTIVE if active else EMOJI_INACTIVE
        
        row.append(InlineKeyboardButton(
            text=f"{check}{prefix}{status_dot} {name}",
            callback_data=f"toggle_{s_id}"
        ))
        
        if len(row) == KEYBOARD_COLS:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    buttons.append([InlineKeyboardButton(text="🚀 ПРИМЕНИТЬ", callback_data="confirm_selection")])
    buttons.append([InlineKeyboardButton(text="🧹 Сбросить выбор", callback_data="clear_current_list")])
    buttons.append([InlineKeyboardButton(text="🚫 Отмена", callback_data="cancel_selection")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
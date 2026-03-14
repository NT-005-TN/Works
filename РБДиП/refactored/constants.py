"""
Константы приложения
"""
from typing import Final

# Emoji константы
EMOJI_PRIORITY: Final[str] = "⭐"
EMOJI_LATE: Final[str] = "🐌"
EMOJI_ADDED: Final[str] = "😭"
EMOJI_ACTIVE: Final[str] = "🟢"
EMOJI_INACTIVE: Final[str] = "🔴"

# Текстовые константы
TEXT_NO_QUEUES: Final[str] = "⚠️ Нет сохранённых очередей!"
TEXT_QUEUE_NOT_FOUND: Final[str] = "⚠️ Очередь не найдена"
TEXT_NO_PERMISSION: Final[str] = "⛔ Нет прав! Знай своё место!"
TEXT_NO_ACTIVE_STUDENTS: Final[str] = "⚠️ Нет активных студентов"

# Ограничения
MAX_SWAP_SELECTION: Final[int] = 2
DEFAULT_WEIGHT: Final[float] = 1.0
MIN_WEIGHT: Final[float] = 0.1
MAX_WEIGHT: Final[float] = 10.0
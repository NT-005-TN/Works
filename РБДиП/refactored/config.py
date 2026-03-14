"""
Конфигурация приложения с валидацией
"""
import os
import sys
from pathlib import Path
from typing import Set, Final
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Админы бота
ADMINS: Final[Set[int]] = {1607498152, 5174581416}

# Токен бота с проверкой
TOKEN: str = os.getenv("BOT_TOKEN") or os.getenv("DEV_TOKEN")
if not TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN или DEV_TOKEN не задан в .env файле!")
    sys.exit(1)

# Параметры алгоритма
K_FACTOR: Final[float] = float(os.getenv("K_FACTOR", "1.0"))

# Ограничения
RECENT_QUEUE_LIMIT: Final[int] = int(os.getenv("RECENT_QUEUE_LIMIT", "5"))
HISTORY_LIMIT: Final[int] = int(os.getenv("HISTORY_LIMIT", "10"))
WEIGHT_HISTORY_LIMIT_PER_STUDENT: Final[int] = int(os.getenv("WEIGHT_HISTORY_LIMIT_PER_STUDENT", "10"))

# База данных
DB_NAME: Final[str] = os.getenv("DB_NAME", "students.db")
DB_PATH: Final[Path] = Path(__file__).parent / DB_NAME

# Логирование
LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO")
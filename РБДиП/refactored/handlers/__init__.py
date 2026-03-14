"""
Обработчики сообщений бота
"""
from aiogram import Router

from .admin import router as admin_router
from .user import router as user_router
from .callbacks import router as callbacks_router

# Создаём главный роутер
router = Router()

# Включаем роутеры
router.include_router(admin_router)
router.include_router(user_router)
router.include_router(callbacks_router)

__all__ = ["router"]
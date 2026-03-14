import os
from flask import Flask
from config import Config
from extensions import db, login_manager
from models import User
from services.image_service import init_reference_hash

# Импорт блюпринтов
from routes.auth import auth_bp
from routes.main import main_bp
from routes.casino import casino_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    
    # Инициализация сервиса (предварительный расчет хеша кокоса)
    with app.app_context():
        init_reference_hash()

    # Регистрация маршрутов (Blueprints)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(casino_bp)
    app.register_blueprint(admin_bp)

    # Создание таблиц БД при первом запуске
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except ValueError:
            return None

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
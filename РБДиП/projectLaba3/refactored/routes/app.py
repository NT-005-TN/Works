
import os
from dotenv import load_dotenv
from flask import Flask
from extensions import db, login_manager
from models import User
from services.image_service import init_reference_hash

# Импорт блюпринтов
from routes.auth import auth_bp
from routes.main import main_bp
from routes.casino import casino_bp
from routes.admin import admin_bp

load_dotenv() # Загрузка переменных окружения

def create_app():
    app = Flask(__name__)
    
    # Конфигурация
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///bank.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    
    # Инициализация сервиса (хеш кокоса)
    with app.app_context():
        init_reference_hash()

    # Регистрация маршрутов
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(casino_bp)
    app.register_blueprint(admin_bp)

    # Создание таблиц БД
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
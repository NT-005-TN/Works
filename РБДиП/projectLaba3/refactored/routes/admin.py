from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from extensions import db
from models import User
from services.image_service import verify_coconut_image
import json

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/panel')
@login_required
def admin_panel():
    # Здесь можно добавить проверку роли админа, если нужно
    return render_template('admin.html')

@admin_bp.route('/verify_admin_image', methods=['POST'])
@login_required
def verify_admin_image():
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'Изображение не найдено'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'Файл не выбран'})
    
    is_match = verify_coconut_image(file)
    return jsonify({'success': is_match})

@admin_bp.route('/get_database')
@login_required
def get_database():
    try:
        users = User.query.all()
        # Конвертируем объекты SQLAlchemy в словари для JSON
        data = {
            u.phone: {
                'name': u.name,
                'phone': u.phone,
                'password': u.password_hash, # В реальном проекте пароли лучше не отдавать
                'money': u.money,
                'card_number': u.card_number,
                'country': u.country,
                'spins_count': u.spins_count
            } for u in users
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/update_database', methods=['POST'])
@login_required
def update_database():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'Файл не найден'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'Файл не выбран'})
    
    try:
        new_data_raw = json.loads(file.read().decode('utf-8'))
        
        # Очистка текущей БД и заполнение новой (осторожно!)
        User.query.delete()
        
        for phone, user_data in new_data_raw.items():
            required_fields = ['name', 'phone', 'password', 'money', 'card_number', 'country']
            if not all(field in user_data for field in required_fields):
                # Откат транзакции при ошибке структуры
                db.session.rollback()
                return jsonify({'success': False, 'error': f'Неверная структура данных для {phone}'})
            
            user = User(
                name=user_data['name'],
                phone=user_data['phone'],
                password_hash=user_data['password'], # Предполагаем, что в файле уже хеш
                money=user_data.get('money', 0),
                card_number=user_data.get('card_number', ''),
                country=user_data.get('country', ''),
                spins_count=user_data.get('spins_count', 0)
            )
            db.session.add(user)
            
        db.session.commit()
        return jsonify({'success': True})
        
    except json.JSONDecodeError:
        db.session.rollback()
        return jsonify({'success': False, 'error': 'Неверный формат JSON'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)})
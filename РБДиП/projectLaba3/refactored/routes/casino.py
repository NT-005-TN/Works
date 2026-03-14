from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user
from extensions import db
from models import User
import random

casino_bp = Blueprint('casino', __name__, url_prefix='/casino')
MAX_SPINS = 10

@casino_bp.route('/', methods=['GET'])
@login_required
def casino_page():
    spins_left = MAX_SPINS - current_user.spins_count
    return render_template('casino.html', spins_left=spins_left)

@casino_bp.route('/', methods=['POST'])
@login_required
def spin():
    # Берем актуальные данные из БД
    user = User.query.get(current_user.id)
    
    if user.spins_count >= MAX_SPINS:
        # Сброс баланса и счетчика
        user.money = 0
        user.spins_count = 0
        db.session.commit()
        return jsonify({
            'result': 'Лимит кручений достигнут. Баланс сброшен.',
            'balance': user.money,
            'final_spin': True,
            'message': 'Не в этот раз'
        })

    # Логика выигрыша: 9 шансов проиграть 20k, 1 шанс выиграть 180k
    results = [-20000] * 9 + [180000]
    result = random.choice(results)
    
    user.money += result
    user.spins_count += 1
    
    db.session.commit()
    
    is_final_spin = (user.spins_count == MAX_SPINS)
    
    response_data = {
        'result': result,
        'balance': user.money,
        'final_spin': is_final_spin,
        'message': 'Поздравляем!' if result > 0 else 'Не в этот раз'
    }
    return jsonify(response_data)

@casino_bp.route('/get_money', methods=['POST'])
@login_required
def get_money():
    user = User.query.get(current_user.id)
    if not user:
        return jsonify({'success': False, 'error': 'User not found'}), 404
        
    amount = random.randint(100, 1000)
    user.money += amount
    db.session.commit()
    return jsonify({'success': True, 'amount': amount})
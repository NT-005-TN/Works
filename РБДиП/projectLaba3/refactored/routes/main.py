from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    # Получаем всех пользователей для лидерборда
    users = User.query.order_by(User.money.desc()).all()
    return render_template('index.html', leaderboard=users)

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
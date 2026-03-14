from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from extensions import db
from models import User
import random

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        password = request.form.get('password')
        country = request.form.get('country')

        if not all([name, phone, password]):
            flash('Все поля обязательны для заполнения')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(name=name).first():
            flash('Это имя уже занято. Пожалуйста, выберите другое.')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(phone=phone).first():
            flash('Этот номер телефона уже зарегистрирован')
            return redirect(url_for('auth.register'))

        card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        
        user = User(name=name, phone=phone, country=country, card_number=card_number)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка регистрации: {str(e)}')
            return redirect(url_for('auth.register'))
        
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(name=username).first()
        
        if not user or not user.check_password(password):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('auth.login'))
            
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.index'))
        
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
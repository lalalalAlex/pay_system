from database.models import User
from database import get_db
from datetime import datetime


def login_user_db(email, password):
    db = next(get_db())
    user = db.query(User).filter_by(email=email).first()
    if user:
        if user.password == password:
            return {'message': 'Вы успешно вошли в аккаунт'}
        else:
            return {'message': 'Пароль введен неверно'}
    else:
        return {'message': 'Пользователь с таким e-mail не найден'}


def register_user_db(name, lastname, email, phone_number, city, password):
    db = next(get_db())
    user = User(name=name, lastname=lastname, email=email, phone_number=phone_number, city=city, password=password, reg_date=datetime.now())
    db.add(user)
    db.commit()
    return {'message': 'Успешно добавлен'}


def get_exact_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    return {'message': {'Пользователь': user}}


def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        return {'message': 'Такого пользователя нет'}
    else:
        db.delete(user)
        db.commit()
        return {'message': 'Успешно удален'}


def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'password':
            exact_user.password = new_data
        elif edit_type == 'city':
            exact_user.city = new_data

        db.commit()
        return {'message': 'Данные успешно изменены'}
    else:
        return {'message': 'Пользователь не найден'}


def check_user_email_db(email):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        return checker
    else:
        return False




from database.models import UserCard
from database import get_db


def checker_card(card_number):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    if checker:
        return 'Карта есть'
    else:
        return False


def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())
    new_card = UserCard(user_id=user_id, card_number=card_number, card_name=card_name, balance=balance,exp_date=exp_date)
    checker = checker_card(card_number)
    if checker:
        return {'status': 0,
                'message': 'Карта уже есть'}
    else:
        db.add(new_card)
        db.commit()
        return {'status': 1,
                'message': {'Карта успешно добавлена. Номер карты': new_card.card_number}}



def get_exact_user_cards_db(user_id):
    db = next(get_db())
    exact_card = db.query(UserCard).filter_by(id=user_id).all()
    return {'message': {'Все карты': exact_card}}


def get_exact_card_db(card_id, user_id):
    db = next(get_db())
    exact_card = db.query(UserCard).filter_by(id=card_id, user_id=user_id).first()
    return {'message': {'Карта': exact_card}}


def check_card_db(card_number):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    return {'message': checker}


def delete_card_db(card_id):
    db = next(get_db())
    delete_card = db.query(UserCard).filter_by(id=card_id).first()
    if delete_card:
        db.delete(delete_card)
        db.commit()
        return {'message': 'Карта успешно удалена'}
    else:
        return {'message': 'Карта не найдена'}

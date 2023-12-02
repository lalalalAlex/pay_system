from database.models import UserTransfers, UserCard
from database import get_db
from datetime import datetime


def validator_cards(card_number, db):
    db = next(get_db())
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()
    return exact_card


def create_transfer_db(card_from, card_to, amount):
    db = next(get_db())
    checker_card_from = validator_cards(card_from, db)
    checker_card_to = validator_cards(card_to, db)
    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount
            checker_card_to.balance += amount
            new_transfer = UserTransfers(card_id_from=card_from, card_id_to=card_to, amount=amount, transfer_date=datetime.now())
            db.add(new_transfer)
            db.commit()
            return {'message': 'Деньши успешно отправлены'}
        else:
            return {'message': 'Не хватает денег для отправки'}
    else:
            return {'message': 'Нет одной из карт'}


def all_transfers_db(card_id_from):
    db = next(get_db())
    transfers = db.query(UserTransfers).filter_by(card_id_from=card_id_from).all()
    return {'message': transfers}


def cancel_card_transfer_db(card_from, card_to, amount, transfer_id):
    pass

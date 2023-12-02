from sqlalchemy import Column, String, Boolean, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class UserCard(Base):
    __tablename__ = 'user_cards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    card_number = Column(String, nullable=False)
    balance = Column(Float, default=0)
    exp_date = Column(Integer, nullable=False)
    card_name = Column(String)

    user_fk = relationship(User, lazy='subquery')


class UserTransfers(Base):
    __tablename__ = 'user_transfers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_id_from = Column(Integer, ForeignKey('user_cards.id'))
    card_id_to = Column(Integer, ForeignKey('user_cards.id'))
    amount = Column(Float)
    status = Column(Boolean, default=True)
    transfer_date = Column(DateTime)

    card_fk_from = relationship(UserCard, foreign_keys=[card_id_from], lazy='subquery')
    card_fk_to = relationship(UserCard, foreign_keys=[card_id_to], lazy='subquery')


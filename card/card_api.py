from fastapi import APIRouter
from database.card_service import check_card_db, delete_card_db, add_card_db, get_exact_card_db, get_exact_user_cards_db
from card import AddCardValidator, GetExactUserCardValidator

card_router = APIRouter(prefix='/card', tags=['Карты и Настройки'])


@card_router.post('/add-card')
async def add_card(data: AddCardValidator):
    add_data = data.model_dump()
    result = add_card_db(**add_data)
    return {'message': result}


@card_router.get('/get-all-cards-user')
async def all_cards(data: GetExactUserCardValidator):
    user_data = data.model_dump()
    result = get_exact_user_cards_db(**user_data)
    return {'message': result}


@card_router.get('/get-exact-card')
async def get_card(card_id: int, user_id: int):
    result = get_exact_card_db(card_id, user_id)
    return {'message': result}


@card_router.delete('/delete-card')
async def delete_card(card_id):
    result = delete_card_db(card_id)
    return {'message': result}
from fastapi import APIRouter
from datetime import datetime
from database.user_service import register_user_db, get_exact_user_db, delete_user_db, check_user_email_db, edit_user_db
from user import EditUserValidator, UserRegistrationValidator

user_router = APIRouter(prefix='/user', tags=['Пользователи и Настройки'])


@user_router.post('/registration-user')
async def register(data: UserRegistrationValidator):
    new_user_data = data.model_dump()
    checker = check_user_email_db(data.email)
    if checker:
        return {'Пользователь уже есть'}
    else:
        result = register_user_db(**new_user_data)
        return {'message': result}


@user_router.get('/information-user')
async def exact_user(user_id: int):
    result = get_exact_user_db(user_id)
    return {'message': result}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)
    return {'message': result}


@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change = data.model_dump()
    result = edit_user_db(**change)
    return {'message': result}
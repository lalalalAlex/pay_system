from database.transfer_service import all_transfers_db, create_transfer_db
from fastapi import APIRouter
from transfers import CreateTransferValidator


transfer_router = APIRouter(prefix='/transaction', tags=['Транзакции и Насторойки'])


@transfer_router.get('/all')
async def all_transfers(card_id: int):
    result = all_transfers_db(card_id)
    return {'message': result}


@transfer_router.post('/create-transaction')
async def create_transfer(data: CreateTransferValidator):
    card = data.model_dump()
    result = create_transfer_db(**card)
    return {'message': result}
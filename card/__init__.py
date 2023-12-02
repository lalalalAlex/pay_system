from pydantic import BaseModel


class AddCardValidator(BaseModel):
    user_id: int
    card_number: str
    card_name: str = 'Карта'
    exp_date: str
    balance: float = 0


class GetExactUserCardValidator(BaseModel):
    user_id: int



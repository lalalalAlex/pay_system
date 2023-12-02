from pydantic import BaseModel


class CreateTransferValidator(BaseModel):
    card_from: str
    card_to: str
    amount: float



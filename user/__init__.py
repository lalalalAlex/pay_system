from pydantic import BaseModel


class UserRegistrationValidator(BaseModel):
    name: str
    lastname: str
    email: str
    phone_number: str
    city: str
    password: str


class ExactUserValidator(BaseModel):
    user_id: int


class DeleteUserValidator(BaseModel):
    user_id: int


class EditUserValidator(BaseModel):
    user_id: int
    edit_type: str
    new_data: str





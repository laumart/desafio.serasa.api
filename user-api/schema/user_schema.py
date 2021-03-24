from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    nome: str
    cpf: str
    email: str
    phone_number: Optional[str] = None


class UserUpdate(BaseModel):
    nome: str
    phone_number: Optional[str] = None
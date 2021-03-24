from schema.user_schema import User, UserUpdate
from models.user import UserBase
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

# Listar, exibir, criar, alterar e excluir usuários


@router.get("/api/user/{id}")
async def get_user(id: int):
    user_db = UserBase()
    return user_db.select_user(id)


@router.get("/api/users")
async def get_users():
    user_db = UserBase()
    return user_db.select_allusers()


@router.post("/api/user", include_in_schema=True, summary="Create User")
async def save_user(usu: User):
    usu_includ = UserBase(nome=usu.nome, cpf=usu.cpf, email=usu.email, phone_number=usu.phone_number)
    usu_includ.save_user()
    return usu_includ


@router.put("/api/user/{id}")
async def update_user(id: str, usu: UserUpdate):
    usu_update = UserBase(nome=usu.nome, phone_number=usu.phone_number)
    usu_update.update_user(id)
    json_converte = jsonable_encoder(usu)
    return JSONResponse(content=json_converte)


@router.delete("/api/user/{id}")
async def delete_user(id: int):
    user_db = UserBase()
    return user_db.delete_user(id)
     







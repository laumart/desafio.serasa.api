from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
import datetime
from db.session import Sessao, Base
from db.cache import client_memcache
from fastapi import HTTPException
from dotenv import load_dotenv
from pathlib import Path
from cryptography.fernet import Fernet
import os
import datetime
import requests
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
cache_update = False

class UserBase(Base):
    __tablename__ = 'user'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String, nullable=False, index=True)
    #cpf: str = Column(String, nullable=False, index=True, unique=True)
    cpf = Column(LargeBinary)
    email: str = Column(String, nullable=False, index=True, unique=True)
    phone_number = Column(String, nullable=True)
    created_at: DateTime = Column(DateTime, default=datetime.datetime.now())
    updated_at: DateTime = Column(DateTime, onupdate=datetime.datetime.now())

    def __init__(self, nome: str = None, cpf: str = None, email: str = None, phone_number: str = None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
       return "{'id':'%s', 'nome':'%s', 'cpf':'%s', 'email':'%s', 'phone_number':'%s'}" % (
                            self.id, self.nome, self.cpf, self.email, self.phone_number)

    def save_user(self):
        global cache_update
        key = os.getenv("KEYDATABASE")
        f = Fernet(key)
        token = f.encrypt(str.encode(self.cpf))
        self.cpf = token
        try:
            session_db = self.get_user_session()
            session_db.add(self)
            session_db.commit()
            cache_update = False
            return session_db.query(UserBase).filter_by(cpf=self.cpf).all()
        except:
            return {'erro': 'erro ao salvar usuario'}

    def select_user(self, id_user: int):
        #res = client_memcache.gets('all_users')
        session_db = self.get_user_session()
        res = session_db.query(UserBase).filter_by(id=id_user).first()
        if not res:
            raise HTTPException(status_code=204, headers={'erro': 'usuario não encontrado'})
        
        key = os.getenv("KEYDATABASE")
        f = Fernet(key)
        res.cpf = f.decrypt(res.cpf)
        return res

    def select_allusers(self):
        global cache_update
        if cache_update:
            res = client_memcache.get('all_users')
            return res
        
        if not cache_update:
            session_db = self.get_user_session()
            res = session_db.query(UserBase).all()
            cache_update = True
            if res:
                client_memcache.set('all_users', res, expire=60*60)
            else:
                raise HTTPException(status_code=204, headers={'erro': 'usuario não encontrado'})    
        return res

    def delete_user(self, id_user: int):
        global cache_update
        #USER_ORDER_URL = f'http://{os.getenv("ORDERAPI_SERVER")}:{os.getenv("ORDERAPI_PORT")}'
        #res_user_order = requests.get(f'{USER_ORDER_URL}/api/order/user/{str(id_user)}')
        #return res_user_order
        #res_user_order=True
        #print(f'{USER_ORDER_URL}/api/order/user/{str(id_user)}')

        #if not res_user_order:
        session_db = self.get_user_session()
        res = session_db.query(UserBase).filter_by(id=id_user).delete(synchronize_session='evaluate')
        if res:
            session_db.commit()
            cache_update = False
            return {'message': 'Usuario deletado com sucesso'}
        else:
            raise HTTPException(status_code=204, headers={'erro': 'usuario não encontrado'})
        #else:
        #    return res_user_order

    def update_user(self, id_user: int):
        global cache_update
        session_db = self.get_user_session()
        res = session_db.query(UserBase).filter_by(id=id_user).first()
        if not res:
            raise HTTPException(status_code=204, headers={'erro': 'usuario não encontrado'})

        try:
            res = session_db.query(UserBase).filter_by(id=id_user). \
                         update({"nome": self.nome, "phone_number": self.phone_number, "updated_at": datetime.datetime.now()}, \
                            synchronize_session='evaluate')
            session_db.commit()
            cache_update = False
            return res
        except:
            return {'erro': 'erro ao alterar usuario'}

    def get_user_session(self):
        sessao = Sessao()
        self.metadata.create_all(sessao.engine)
        session_db = sessao.get_session()
        return session_db

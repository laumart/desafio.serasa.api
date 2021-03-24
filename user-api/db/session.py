from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
from pathlib import Path
import os


Base = declarative_base()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Sessao():

    def __init__(self):
        self.DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_SERVER")}:{os.getenv("POSTGRES_PORT")}/serasa'
        self.engine = create_engine(self.DATABASE_URL, echo=False)
        try:
            if not database_exists(self.engine.url):
                create_database(self.engine.url)
        except ConnectionError as err:
            return print(f'Não foi possivel conectar com a base de dados {err}')

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

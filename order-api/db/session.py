from typing import Any
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Sessao():

    def __init__(self):
        self.ELASTIC_URL = f'http://{os.getenv("ELASTICSEARCH_SERVER")}:{os.getenv("ELASTICSEARCH_PORT")}'

        try:
            self.es = Elasticsearch(self.ELASTIC_URL, scheme="http")
        except ConnectionError as err:
            return print(f'Não foi possivel conectar com a base de dados {err}')
            exit(1)

    def get_session(self):
        if not self.es.indices.exists(index="orders"):
            # ignore 400 cause by IndexAlreadyExistsException when creating an index
            self.es.indices.create(index="orders", ignore=400)

        return self.es

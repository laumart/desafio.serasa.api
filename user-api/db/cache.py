import json
from pymemcache.client.base import Client
from pymemcache import serde
from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client_memcache = Client((os.getenv("MEMCACHE_SERVER"), os.getenv("MEMCACHE_PORT")), serde=serde.pickle_serde)

"""
TESTE DE CACHE

client = Client(('127.0.0.1', 11211), serde=JsonSerde())
client.set('key', {'a': 'b', 'c': 'd'})
result = client.get('key')

print(result)
"""
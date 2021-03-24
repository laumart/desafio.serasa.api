import json
from pymemcache.client.base import Client
from dotenv import load_dotenv
from pathlib import Path
import os

class JsonSerde(object):
    def serialize(self, key, value):
        if isinstance(value, str):
            return value, 1
        return json.dumps(value), 2

    def deserialize(self, key, value, flags):
       if flags == 1:
           return value
       if flags == 2:
           return json.loads(value)
       raise Exception("Unknown serialization format")


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client_memcache = Client((os.getenv("MEMCACHE_SERVER"), os.getenv("MEMCACHE_PORT")))

#client_memcache = Client(('127.0.0.1', 11211), serde=JsonSerde())
#client_memcache = Client(('127.0.0.1', 11211))

"""
TESTE DE CACHE

client = Client(('127.0.0.1', 11211), serde=JsonSerde())
client.set('key', {'a': 'b', 'c': 'd'})
result = client.get('key')

print(result)
"""
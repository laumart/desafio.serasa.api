from db.session import Sessao
from db.cache import client_memcache
from schema.order_schema import Order, OrderUpdate
from fastapi import HTTPException
from dotenv import load_dotenv
from pathlib import Path
import os
import datetime
import requests

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class OrderBase():
    def __init__(self):
        self.USER_API_URL = f'http://{os.getenv("USERAPI_SERVER")}:{os.getenv("USERAPI_PORT")}'

    def save_order(self, order: Order):
        res_user = requests.get(f'{self.USER_API_URL}/api/user/{str(order.user_id)}')
        
        if res_user.status_code == 204:
            raise HTTPException(status_code=204, headers={"error":"User Not Found"})

        doc = {
            'user_id': order.user_id,
            'item_description': order.item_description,
            'item_quantity': order.item_quantity,
            'item_price': order.item_price,
            'total_value': order.item_price * order.item_quantity,
            'created_at': datetime.datetime.now(),
            'updated_at': ''
        }

        session_es = self.get_order_session()
        order = session_es.index(index='orders', doc_type='_doc', body=doc)
        return doc

    def select_order(self, order_id: str):
        query = {
            "size": 100,
            "query": {
                "match": {"_id": order_id}
            }
        }
        session_db = self.get_order_session()
        order = session_db.search(index="orders", doc_type="_doc", body=query)['hits']
        array_orders = []
        object_order = {}
        if order['hits']:
            for item in order['hits']:
                doc = {
                    'id': item['_id'],
                    'user_id': item['_source']['user_id'],
                    'item_description': item['_source']['item_description'],
                    'item_quantity': item['_source']['item_quantity'],
                    'item_price': item['_source']['item_price'],
                    'total_value': item['_source']['total_value'],
                    'created_at': item['_source']['created_at'],
                    'updated_at': item['_source']['updated_at']
                }
                array_orders.append(doc)
            if array_orders:
                object_order = array_orders[0]
            return object_order
        else:
            return HTTPException(status_code=204, headers={'error':'Order Not Found'})

    def select_order_by_user(self, user_id: int):
        res = requests.get(self.USER_API_URL + "/api/user/" + str(user_id))
        if res.status_code == 204:
            return HTTPException(status_code=204, headers={'error':'User Not Found'})

        query = {
            "size": 10000,
            "query": {
                "match": {"user_id": user_id}}
        }
        session_db = self.get_order_session()
        orders = session_db.search(index="orders", doc_type="_doc", body=query, scroll='1m')['hits']
        array_orders = []
        if orders['hits']:
            for item in orders['hits']:
                doc = {
                    'id': item['_id'],
                    'user_id': item['_source']['user_id'],
                    'item_description': item['_source']['item_description'],
                    'item_quantity': item['_source']['item_quantity'],
                    'item_price': item['_source']['item_price'],
                    'total_value': item['_source']['total_value'],
                    'created_at': item['_source']['created_at'],
                    'updated_at': item['_source']['updated_at']
                }
                array_orders.append(doc)
            return array_orders
        return HTTPException(status_code=204, headers={'error':'Order Not Found'})

    def select_allorders(self):
        query = {
            "size": 10000,
            "query": {"match_all": {}}
        }
        session_es = self.get_order_session()
        orders = session_es.search(index="orders", doc_type="_doc", body=query, scroll='1m')['hits']
        array_orders = []        
        if orders['hits']:
            for item in orders['hits']:
                doc = {
                    'id': item['_id'],
                    'user_id': item['_source']['user_id'],
                    'item_description': item['_source']['item_description'],
                    'item_quantity': item['_source']['item_quantity'],
                    'item_price': item['_source']['item_price'],
                    'total_value': item['_source']['total_value'],
                    'created_at': item['_source']['created_at'],
                    'updated_at': item['_source']['updated_at']
                }
                array_orders.append(doc)
        else:
            return HTTPException(status_code=204, headers={'error':'Orders Not Found'})
        return array_orders
        

    def delete_order(self, order_id: str):
        try:
            session_db = self.get_order_session()
            session_db.delete(index='orders', doc_type='_doc', id=order_id)
            return {'message': 'Order deleted'}
        except:
            return {'error': 'Delete Order'}

    def update_order(self, order_id: str, order: OrderUpdate):
        try:
            original_order = self.select_order(order_id)
            
            if hasattr(original_order, 'status_code'):
                if original_order.status_code == 204:
                    return original_order
            
            data_obj = {
                'user_id': original_order['user_id'],
                'item_description': original_order['item_description'],
                'item_quantity': original_order['item_quantity'],
                'item_price': original_order['item_price'],
                'total_value': original_order['total_value'],
                'created_at': original_order['created_at'],
                'updated_at': original_order['updated_at']
            }

            if order.item_description:
                data_obj['item_description'] = order.item_description

            if order.item_quantity:
                data_obj['item_quantity'] = order.item_quantity

            if order.item_price:
                data_obj['item_price'] = order.item_price

            data_obj['total_value'] = data_obj['item_quantity'] * data_obj['item_price']
            data_obj['updated_at'] = datetime.datetime.now()
            session_es = self.get_order_session()
            session_es.index(index='orders', doc_type='_doc', id=order_id, body=data_obj)
            return data_obj
        except:
            return HTTPException(status_code=500)

    def get_order_session(self):
        sessao = Sessao()
        session_db = sessao.get_session()
        return session_db
import json
import pytest
from fastapi.testclient import TestClient
from tests.utils import random_lower_string, random_id_user, random_item_quantity, random_item_price
from main import app
import datetime

user_id = random_id_user()
order_id: str = 'XRNeYHcBfziIT92BEIVL'
description = random_lower_string()
quantity = random_item_quantity()
price = random_item_price()

@pytest.fixture(scope='session')
def client():
    client = TestClient(app)
    return client


def test_save_order(client):
    global user_id
    global description
    global price
    global quantity
    doc = {
        'user_id': 1,
        'item_description': description,
        'item_quantity': quantity,
        'item_price': price
    }
    response = client.post('/api/order', json=doc)
    assert response.status_code == 201


def test_save_order_user_not_found(client):
    global user_id
    global description
    global price
    global quantity
    doc = {
        'user_id': 2,
        'item_description': description,
        'item_quantity': quantity,
        'item_price': price,
        'total_value': quantity * price
    }
    response = client.post('/api/order', json=doc)
    assert response.status_code == 404


def test_get_orders(client):
    response = client.get('/api/orders')

    # status_code = 200
    assert response.status_code == 200
    assert len(str(response.json)) > 0


def test_get_order(client):
    global order_id
    response = client.get('/api/order/' + str(order_id))
    # status_code = 200 & not is empty
    assert response.status_code == 200
    assert len(str(response.json)) > 0


def test_get_order_by_user(client):
    global user_id
    response = client.get('/api/order/user/' + str(user_id))
    # status_code = 200 & not is empty
    assert response.status_code == 200


def test_update_order(client):
    global order_id
    global description
    global price
    global quantity
    doc = {
        'item_description': description,
        'item_quantity': quantity,
        'item_price': price
    }
    response = client.put('/api/order/' + order_id, json=doc)
    assert response.status_code == 200


def test_delete_order(client):
    global order_id
    response = client.delete('/api/order/' + order_id)
    assert response.status_code == 200


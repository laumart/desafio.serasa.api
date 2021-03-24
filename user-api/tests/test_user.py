import json
import pytest
from fastapi.testclient import TestClient
from tests.utils import random_email, random_lower_string, random_id_user
from main import app

userid = random_id_user()
username = random_lower_string()


@pytest.fixture(scope='session')
def client():
    client = TestClient(app)
    return client


def test_get_user(client):
    global userid
    response = client.get('/api/usuario/' + str(userid))
    # status_code = 200 & not is empty
    assert response.status_code == 200
    assert len(str(response.json)) > 0


def test_get_usuarios(client):
    response = client.get('/api/usuarios')

    # status_code = 200
    assert response.status_code == 200
    assert len(str(response.json)) > 0


def test_save_usuario(client):
    global userid
    global username
    doc = {
        'nome': username,
        'cpf': '01234567890',
        'email': 'user@test.com',
        'phone_number': '11900001111'
    }
    response = client.post('/api/usuario', json=doc)
    #userid = response.json['id']
    # assert response.json == 'sda'
    assert response.status_code == 201


def test_update_usuario(client):
    global userid
    doc = {
        'nome': 'Test Updated',
        'phone_number': '1132841393'
    }
    response = client.put('/api/usuario/' + str(userid), json=doc)
    assert response.status_code == 200


def test_delete_usuario(client):
    global userid
    response = client.delete('/api/usuario/' + str(userid))

    # status_code = 200 & not is empty
    assert response.status_code == 200
    assert len(str(response.json)) > 0


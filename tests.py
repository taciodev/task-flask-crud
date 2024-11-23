import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture
def create_task():
    new_task_data = {
        'title': 'Fazer compras',
        'description': 'Comprar leite, pão e ovos no supermercado.'
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    task_id = response_json.get('id')
    yield task_id
    # Cleanup: Exclua a tarefa após o teste
    requests.delete(f'{BASE_URL}/tasks/{task_id}')

def test_create_task():
    new_task_data = {
        'title': 'Fazer compras',
        'description': 'Comprar leite, pão e ovos no supermercado.'
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert 'message' in response_json
    assert 'id' in response_json

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json

def test_get_task(create_task):
    task_id = create_task
    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json.get('id')

def test_update_task(create_task):
    task_id = create_task
    payload = {
        'title': 'Fazer compras no supermercado',
        'description': 'Comprar ovos, pão, queijo e presunto no supermercado.',
        'completed': True
    }
    response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert 'message' in response_json

    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get('title') == payload.get('title')
    assert response_json.get('description') == payload.get('description')
    assert response_json.get('completed') == payload.get('completed')

def test_delete_task(create_task):
    task_id = create_task
    response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200
    response_json = response.json()
    assert 'message' in response_json

    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 404
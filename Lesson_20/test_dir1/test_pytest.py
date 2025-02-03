import random
import requests
import pytest
import time


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('Bye')


@pytest.mark.smoke
def test_get_one_post(new_post_id, hello):
    print('test')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.smoke
def test_get_all_posts(hello):
    print('test')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@pytest.mark.regression
def test_add_post(hello):
    print('test')
    body = {
        "title": "VItya",
        "body": "Vitek",
        "userId": "1511"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()['id'] == 101

@pytest.mark.regression
def test_one():
    #time.sleep(3)
    assert 1 == 1

@pytest.mark.parametrize('logins', [1,2,3,4])
def test_two(logins):
    print(logins)
    #time.sleep(3)
    assert 1 == 1

def test_three():
    #time.sleep(3)
    assert 1 == 1
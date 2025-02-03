import requests
import pytest

@pytest.fixture()
def num():
    return 3

def test_delete(new_post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')



def test_num(num):
    print(num)

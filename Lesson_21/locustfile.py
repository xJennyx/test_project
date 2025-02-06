from locust import task, HttpUser
import random


class ResourceUser(HttpUser):

    #token = None

    # def on_start(self):
    #     response = self.client.post(
    #         '/register',
    #         json={'username': 'Viktor'}
    #     )
    #     self.token = response.json()['token']

    @task(1)
    def get_all_users(self):
        self.client.get(
            '/users',
            headers={'accept': 'application/json'}
        )

    @task(3)
    def get_one_user(self):
        self.client.get(
            f'/users/{random.choice([1, 3, 6, 4])}',
            headers={'accept': 'application/json'}
        )

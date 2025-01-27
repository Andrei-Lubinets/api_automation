from locust import task, HttpUser
from endpoints.endpoint import Endpoint


class ObjectUser(HttpUser, Endpoint):
    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'login': 'Andrei',
            'password': '1241fsdg',
            'admin': false
            }
        )
        self.token = response.json()['token']
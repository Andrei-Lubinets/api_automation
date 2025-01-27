import allure
import requests
from endpoints.endpoint import Endpoit


class ApiPost(Endpoit):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": self.token}

    @allure.step('Add new meme')
    def add_new_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
            self.json = self.response.json()
            self.meme_id = self.json['id']
        except json.JSONDecodeError:
            self.json = None
        return self.response

import json
import requests
import allure
from endpoints.endpoint import Endpoint


class ApiPut(Endpoint):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": self.token}

    @allure.step('Complete modification of object data')
    def change_all_data_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f"{self.url}/meme/{meme_id}", json=payload, headers=headers)
        self.json = self.response.json()
        print(json.dumps(self.json, indent=4))
        return self.response

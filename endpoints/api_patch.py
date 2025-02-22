import allure
import requests
import json
from endpoints.endpoint import Endpoint


class ApiPatch(Endpoint):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": self.token}

    @allure.step('Partial modification of meme data')
    def change_meme_data(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.patch(f"{self.url}/meme/{meme_id}", json=payload, headers=headers)
            self.json = self.response.json()
            print(json.dumps(self.json, indent=4))
        except json.JSONDecodeError:
            self.json = None
        return self.response

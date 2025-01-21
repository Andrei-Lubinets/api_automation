import json
import requests
import allure
from endpoints.endpoint import Endpoit


class ApiPut(Endpoit):
    @allure.step('Complete modification of object data')
    def change_meme(self, meme_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f"{self.url}/meme/{meme_id}", json=payload, headers=headers)
        self.json = self.response.json()
        print(json.dumps(self.json, indent=4))
        return self.response

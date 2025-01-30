import json
import requests
import allure
from endpoints.endpoint import Endpoint


class ApiGet(Endpoint):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": self.token}

    @allure.step('Show all memes')
    def show_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.get(f'{self.url}/meme', headers=headers)
            self.json = self.response.json()
            print(json.dumps(self.json, indent=4))
        except json.JSONDecodeError:
            self.json = None
        return self.response

    @allure.step('Show one meme')
    def show_one_meme(self, headers=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.get(f'{self.url}/meme/1', headers=headers)
            self.json = self.response.json()
            print(json.dumps(self.json, indent=4))
        except json.JSONDecodeError:
            self.json = None
        return self.response

    @allure.step('Show current meme')
    def show_current_meme(self, headers=None, meme_id=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
            text = "404 Not Found"
            if text in self.response.text:
                print(f"Meme with id {meme_id} not found. Status code 404")
            self.json = self.response.json()
            print(json.dumps(self.json, indent=4))
        except json.JSONDecodeError:
            self.json = None
        return self.response, self.response.status_code

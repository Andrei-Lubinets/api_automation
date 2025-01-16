import json
import requests
import allure
from endpoints.endpoint import Endpoit


class ApiGet(Endpoit):

    @allure.step('Show all memes')
    def show_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.json = self.response.json()
        print(json.dumps(self.json, indent=4))
        return self.response

    @allure.step('Show one meme')
    def show_one_meme(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/1', headers=headers)
        self.json = self.response.json()
        print(json.dumps(self.json, indent=4))
        return self.response

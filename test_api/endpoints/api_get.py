import requests
import allure
from endpoint import Endpoit


class ApiGet(Endpoit):

    @allure.step('Show all memes')
    def show_all_memes(self):
        self.response = requests.get(f'{self.url}/meme')
        self.json = self.response.json()
        return self.response

    @allure.step('Show one meme')
    def show_one_meme(self):
        self.response = requests.get(f'{self.url}/meme/1')
        self.json = self.response.json()
        return self.response

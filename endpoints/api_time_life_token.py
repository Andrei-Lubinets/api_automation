import requests
import allure
from endpoint import Endpoit


class ApiAuthorize(Endpoit):
    token = None
    user = None

    @allure.step('Checking if the token is alive')
    def token_is_alive(self, token=None, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/authorize/{self.token}', headers=None)

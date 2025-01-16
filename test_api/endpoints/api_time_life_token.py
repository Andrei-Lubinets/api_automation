import requests
import allure
from endpoint import Endpoit


class ApiAuthorize(Endpoit):
    token = None
    user = None

    @allure.step('Checking if the token is alive')
    def token_is_alive(self, payload, headers=None, token):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize/{self.token}', json=payload, headers=None)

import requests
import allure
from endpoints.endpoint import Endpoit


class ApiAuthorize(Endpoit):
    token = None
    user = None

    @allure.step('Make authorization')
    def make_authorization(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize', json=payload, headers=headers)
        self.json = self.response.json()
        self.token = self.json['token']
        self.user = self.json['user']
        self.headers = {"Authorization": self.token}
        return self.headers, self.token, self.response

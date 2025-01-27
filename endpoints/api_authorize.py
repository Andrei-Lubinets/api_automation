import json

import requests
import allure
from endpoints.endpoint import Endpoint


class ApiAuthorize(Endpoint):
    token = None
    user = None

    @allure.step('Make authorization')
    def make_authorization(self, payload, headers=None):
        headers = headers if headers else self.headers
        try:
            self.response = requests.post(f'{self.url}/authorize', json=payload, headers=headers)
            self.json = self.response.json()
            self.token = self.json['token']
            self.user = self.json['user']
            self.headers = {"Authorization": self.token}
        except json.JSONDecodeError:
            self.json = None
        return self.response

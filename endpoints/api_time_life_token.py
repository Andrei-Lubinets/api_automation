import requests
import allure
from endpoints.endpoint import Endpoit


class ApiLifeAuthorize(Endpoit):
    token = None
    user = None

    @allure.step('Checking if the token is alive')
    def token_is_alive(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/authorize/{self.token}', headers=headers)
        print(self.response)
        text = f"Token is alive"
        if text in self.response.text:
            print("The token is valid")
        else:
            print("The token is invalid")
        return self.response


import requests
import allure
from endpoints.endpoint import Endpoit


class ApiLifeAuthorize(Endpoit):
    @allure.step('Checking if the token is alive')
    def token_is_alive(self, token):
        self.response = requests.get(f'{self.url}/authorize/{token}')
        text = "Token is alive"
        print(self.response.text)
        if text in self.response.text:
            print("The token is valid")
        else:
            print("The token is invalid")
        return self.response

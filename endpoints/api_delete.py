import requests
import allure
from endpoints.endpoint import Endpoit


class ApiDelete(Endpoit):
    @allure.step('Delete meme')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)
        if self.response.text == f'Meme with id {meme_id} successfully deleted':
            print(f"Meme with id {meme_id} has been deleted")
        else:
            print(f"Meme with id {meme_id} not deleted")
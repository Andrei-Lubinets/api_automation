import requests
from endpoints.endpoint import Endpoit


class ApiPost(Endpoit):
    meme_id = None

    def add_new_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=payload, headers=headers)
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response


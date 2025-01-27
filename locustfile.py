import json
from locust import task, HttpUser
from endpoints.endpoint import Endpoint


class ObjectUser(HttpUser, Endpoint):
    token = None
    user = None

    def on_start(self, headers=None):
        headers = headers if headers else self.headers
        payload = {"name": "Batman"}
        try:
            self.response = self.client.post('/authorize', json=payload, headers=headers)
            self.json = self.response.json()
            self.token = self.json['token']
            self.user = self.json['user']
            self.headers = {"Authorization": self.token}
        except json.JSONDecodeError:
            self.json = None
        return self.response, self.headers

    @task
    def get_all_objects(self):
        self.client.get('/meme', headers=self.headers)

    @task
    def get_one_object(self):
        self.client.get('/meme/1', headers=self.headers)

    @task
    def create_meme(self):
        payload = {"info": {"colors": ["brown", "grey", "yellow"], "objects": ["picture", "text"]},
                   "tags": ["fun", "little girl", "fire", "spider"],
                   "text": "There was a spider. It`s gone now.",
                   "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                          ":ANd9GcS20iBpZlg_uZLSnBh8tVZFJvh-JPlYOZe1Hw&s"}
        request = self.client.post('/meme', json=payload, headers=self.headers)
        self.meme_id = request.json()["id"]
        return self.meme_id

    @task
    def change_all_data_meme(self):
        payload = {"id": self.meme_id, "info": {"colors": ["black", "white"], "objects": ["picture", "text", "human"]},
                   "tags": ["really situation", "Nicolas"], "text": "You don`t say?",
                   "url": "https://preview.redd.it/favorite-celebrity-memes-edits-that-never-fail-to-make-you-v0"
                          "-72obmtpl7prb1.jpeg?width=894&format=pjpg&auto=webp&s"
                          "=88f9ae5932382e50c8545ef12704fa02db904209"}
        self.client.put(f'/meme/{self.meme_id}', json=payload, headers=self.headers)

    @task
    def delete_meme(self):
        self.client.delete(f'/meme/{self.meme_id}', headers=self.headers)

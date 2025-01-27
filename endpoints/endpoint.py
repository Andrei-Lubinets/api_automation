import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}
    meme_id = None

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        print(f"Status code {self.response.status_code}")
        assert self.response.status_code == 200

    @allure.step('Check that text is the same as sent')
    def check_that_text_is_correct(self, text):
        assert self.json['text'] == text

    @allure.step('Check that colors is the same as sent')
    def check_that_colors_is_correct(self, colors):
        assert self.json['info']['colors'] == colors

    @allure.step('Check that objects is the same as sent')
    def check_that_objects_is_correct(self, objects):
        assert self.json['info']['objects'] == objects

    @allure.step('Check that tags is the same as sent')
    def check_that_tags_is_correct(self, tags):
        assert self.json['tags'] == tags

    @allure.step('Check that url is the same as sent')
    def check_that_url_is_correct(self, url):
        assert self.json['url'] == url

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        print(f"Status code {self.response.status_code}")
        assert self.response.status_code == 400

    @allure.step('Check that 401 error received')
    def check_no_authorize_request(self):
        print(f"Status code {self.response.status_code}")
        assert self.response.status_code == 401

    @allure.step('Check that 403 error received')
    def check_that_status_is_forbidden_403(self):
        print(f"Status code {self.response.status_code}")
        assert self.response.status_code == 403

    @allure.step('Check that 405 error received')
    def check_method_not_allowed(self):
        print(f"Status code {self.response.status_code}")
        assert self.response.status_code == 405

    @allure.step('Check that user is the same as sent')
    def check_that_user_is_correct(self, user):
        assert self.json['user'] == user

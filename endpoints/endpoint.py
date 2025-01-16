import allure


class Endpoit:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}
    token = None

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that text is the same as sent')
    def check_that_tittle_is_correct(self, text):
        assert self.json['text'] == text

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400

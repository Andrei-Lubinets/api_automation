import pytest
from endpoints.api_get import ApiGet
from endpoints.api_authorize import ApiAuthorize
from endpoints.api_post import ApiPost


@pytest.fixture()
def create_get_endpoint():
    return ApiGet()


@pytest.fixture()
def create_authorize_endpoint():
    return ApiAuthorize()


@pytest.fixture()
def create_new_meme():
    return ApiPost()


@pytest.fixture()
def getting_a_token(create_authorize_endpoint):
    payload = {'name': 'Aladin'}
    create_authorize_endpoint.make_authorization(payload)
    yield create_authorize_endpoint.headers


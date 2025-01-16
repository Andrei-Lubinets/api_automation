import pytest
from endpoints.api_get import ApiGet
from endpoints.api_authorize import ApiAuthorize
from endpoints.api_post import ApiPost
from endpoints.api_time_life_token import ApiLifeAuthorize


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
def check_token_life():
    return ApiLifeAuthorize()


@pytest.fixture()
def getting_a_token(create_authorize_endpoint):
    payload = {'name': 'Aladin'}
    create_authorize_endpoint.make_authorization(payload)
    yield create_authorize_endpoint.headers




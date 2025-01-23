import pytest
from endpoints.api_get import ApiGet
from endpoints.api_authorize import ApiAuthorize
from endpoints.api_post import ApiPost
from endpoints.api_time_life_token import ApiLifeAuthorize
from endpoints.api_put import ApiPut
from endpoints.api_delete import ApiDelete
from endpoints.api_patch import ApiPatch


@pytest.fixture()
def create_get_endpoint(getting_a_token):
    return ApiGet(getting_a_token)


@pytest.fixture()
def create_authorize_endpoint():
    return ApiAuthorize()


@pytest.fixture()
def create_post_endpoint(getting_a_token):
    return ApiPost(getting_a_token)


@pytest.fixture()
def check_authorize_endpoint():
    return ApiLifeAuthorize()


@pytest.fixture()
def create_put_endpoint(getting_a_token):
    return ApiPut(getting_a_token)


@pytest.fixture()
def create_delete_endpoint(getting_a_token):
    return ApiDelete(getting_a_token)


@pytest.fixture()
def create_patch_endpoint(getting_a_token):
    return ApiPatch(getting_a_token)


@pytest.fixture(scope='session')
def getting_a_token():
    payload = {'name': 'Aladin'}
    create_authorize_endpoint = ApiAuthorize()
    create_authorize_endpoint.make_authorization(payload)
    yield create_authorize_endpoint.token


@pytest.fixture()
def getting_meme_id(create_post_endpoint, getting_a_token):
    headers = {"Authorization": getting_a_token}
    data = {
        "info": {
            "colors": [
                "brown",
                "gold",
                "white",
                "black"
            ],
            "objects": [
                "picture",
                "text"
            ]},
        "tags": [
            "fun",
            "Leonardo DiCaprio",
            "Django Unchained"
        ],
        "text": "Моя девушка: Куда с моей карты пропали 45 тысячь рублей?!",
        "url": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65c882eca25d3b73d1124b00_65c886239bb1c5686a10ecd1"
               "/scale_1200"
    }
    create_post_endpoint.add_new_meme(payload=data, headers=headers)
    yield create_post_endpoint.meme_id

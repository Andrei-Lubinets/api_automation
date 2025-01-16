import pytest
from test_api.endpoints.api_get import ApiGet
from test_api.endpoints.api_authorize import ApiAuthorize


@pytest.fixture()
def create_get_endpoint():
    return ApiGet()


@pytest.fixture()
def create_authorize_endpoint():
    return ApiAuthorize()


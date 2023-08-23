import pytest
import time
from jsonschema import validate

import settings
from utils.api import Api
from schemas import disk_schema as schema


@pytest.fixture()
def api_create_data():
    yield settings.API_URL, settings.PUT, settings.CREATE_P, settings.AUTH_HEADER, settings.CODE_201
    time.sleep(1.0)  # Just for insurance
    Api(settings.API_URL).folder(settings.DELETE, settings.DELETE_P, settings.AUTH_HEADER)


def test_create_folder(api_create_data):
    url, method, prefix, headers, code = api_create_data
    response = Api(url).folder(method, prefix, headers)
    validate(instance=response.json(), schema=schema.create_schema)
    assert response.status_code == code

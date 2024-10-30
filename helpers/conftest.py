import pytest
import allure

from helpers.api_service import ApiService
from helpers.payload_builder import PayloadBuilder


@allure.step('Создать основного юзера')
@pytest.fixture
def user_token():
    payload = PayloadBuilder.make_user_create_payload()
    response = ApiService.create_user(payload)
    access_token = response.json().get("accessToken")
    yield access_token
    ApiService.delete_user(access_token)


@allure.step('Создать дополнительного юзера')
@pytest.fixture
def second_user_token():
    payload = PayloadBuilder.make_user_create_payload()
    response = ApiService.create_user(payload)
    access_token = response.json().get("accessToken")
    yield access_token
    ApiService.delete_user(access_token)

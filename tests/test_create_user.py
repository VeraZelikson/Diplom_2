import pytest
import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder


class TestCreatingUser:
    @allure.title('Успешная регистранция уникального юзера')
    def test_successful_user_registration(self):
        payload = PayloadBuilder.make_user_create_payload()
        response = ApiService.create_user(payload)
        user = response.json().get("user")
        assert (response.status_code == 200
                and user.get("email") == payload.get("email")
                and user.get("name") == payload.get("name")
                and response.json().get("accessToken") is not None
                and response.json().get("refreshToken") is not None)

    @allure.title('Регистрация уже существующего юзера')
    def test_user_duplicate(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        response = ApiService.create_user(payload)
        assert response.status_code == 403 and response.json() == ExpectedResponses.CREATE_USER_DUPLICATE_RESPONSE

    @pytest.mark.parametrize(
        'payload',
        [
            PayloadBuilder.make_user_create_payload(with_email=False),
            PayloadBuilder.make_user_create_payload(with_password=False),
            PayloadBuilder.make_user_create_payload(with_name=False),
            PayloadBuilder.make_user_create_payload(with_email=False, with_password=False),
            PayloadBuilder.make_user_create_payload(with_email=False, with_name=False),
            PayloadBuilder.make_user_create_payload(with_name=False, with_password=False),
            PayloadBuilder.make_user_create_payload(with_email=False, with_name=False),
            PayloadBuilder.make_user_create_payload(with_email=False, with_password=False, with_name=False)
        ]
    )
    @allure.title('Создание юзера с отсутствием обязательных полей')
    def test_create_user_with_missing_field(self, payload):
        response = ApiService.create_user(payload)
        assert response.status_code == 403 and response.json() == ExpectedResponses.CREATE_USER_MISSING_FIELDS_RESPONSE

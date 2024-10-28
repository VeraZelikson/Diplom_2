import pytest
import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder


class TestUserLogin:
    @allure.title('Успешная авторизация пользователя')
    def test_successful_user_login(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        response = ApiService.login_user(payload)
        user = response.json().get("user")
        assert (response.status_code == 200
                and response.json().get("success") is True
                and user.get("email") == payload.get("email")
                and user.get("name") == payload.get("name")
                and response.json().get("accessToken") is not None
                and response.json().get("refreshToken") is not None)

    @allure.title('Авторизация с неверным паролем')
    def test_login_with_incorrect_password(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        wrong_password_payload = PayloadBuilder.make_login_payload(
            email=payload.get("email"),
            password="wrong_password"
        )
        response = ApiService.login_user(wrong_password_payload)
        assert (response.status_code == 401
                and response.json() == ExpectedResponses.LOGIN_INVALID_CREDENTIALS_RESPONSE)

    @allure.title('Авторизация с неверным логином')
    def test_login_with_incorrect_email(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        wrong_email_payload = PayloadBuilder.make_login_payload(
            email="wrong_email@example.com",
            password=payload.get("password")
        )
        response = ApiService.login_user(wrong_email_payload)
        assert (response.status_code == 401
                and response.json() == ExpectedResponses.LOGIN_INVALID_CREDENTIALS_RESPONSE)



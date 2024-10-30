import pytest
import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.fakedata import FakeData
from helpers.conftest import user_token, second_user_token


class TestUpdateUserInfo:
    @allure.title('Успешное изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize(
        "update_field, new_value",
        [
            ("email", FakeData.generate_random_email()),
            ("name", FakeData.generate_random_name()),
        ]
    )
    def test_update_user_info_with_auth(self, update_field, new_value, user_token):
        update_payload = {update_field: new_value}
        update_response = ApiService.update_user(update_payload, token=user_token)
        updated_user = update_response.json().get("user")
        assert (update_response.status_code == 200
                and update_response.json().get("success") is True
                and updated_user.get(update_field) == new_value)

    @allure.title('Попытка изменения данных пользователя без авторизации')
    @pytest.mark.parametrize(
        "update_field, new_value",
        [
            ("email", FakeData.generate_random_email()),
            ("name", FakeData.generate_random_name()),
        ]
    )
    def test_update_user_info_without_auth(self, update_field, new_value):
        update_payload = {update_field: new_value}
        update_response = ApiService.update_user(update_payload, '')
        assert (update_response.status_code == 401
                and update_response.json() == ExpectedResponses.UPDATE_USER_INFO_UNAUTHORIZED_RESPONSE)

    @allure.title('Попытка изменения данных пользователя на занятый email')
    def test_update_user_info_with_duplicated_email(self, user_token, second_user_token):
        user2 = ApiService.get_user_info(second_user_token)

        update_payload = {'email': user2.json().get('email')}
        update_response = ApiService.update_user(update_payload, token=user_token)
        assert (update_response.status_code == 403
                and update_response.json() == ExpectedResponses.UPDATE_USER_INFO_EMAIL_EXISTS_RESPONSE)

import pytest
import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.fakedata import FakeData
from helpers.payload_builder import PayloadBuilder


class TestUpdateUserInfo:
    @allure.title('Успешное изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize(
        "update_field, new_value",
        [
            ("email", FakeData.generate_random_email()),
            ("name", FakeData.generate_random_name()),
        ]
    )
    def test_update_user_info_with_auth(self, update_field, new_value):
        response = ApiService.create_user()
        access_token = response.json().get("accessToken")
        update_payload = {update_field: new_value}
        update_response = ApiService.update_user(update_payload, token=access_token)
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
        ApiService.create_user()
        update_payload = {update_field: new_value}
        update_response = ApiService.update_user(update_payload, '')
        assert (update_response.status_code == 401
                and update_response.json() == ExpectedResponses.UPDATE_USER_INFO_UNAUTHORIZED_RESPONSE)

    @allure.title('Попытка изменения данных пользователя на занятый email')
    def test_update_user_info_with_duplicated_email(self):
        payload2 = PayloadBuilder.make_user_create_payload()
        user2 = ApiService.create_user(payload2).json().get('user')

        payload = PayloadBuilder.make_user_create_payload()
        response = ApiService.create_user(payload)
        access_token = response.json().get("accessToken")
        update_payload = {'email': user2.get('email')}
        update_response = ApiService.update_user(update_payload, token=access_token)
        assert (update_response.status_code == 403
                and update_response.json() == ExpectedResponses.UPDATE_USER_INFO_EMAIL_EXISTS_RESPONSE)

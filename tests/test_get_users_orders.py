import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder
from helpers.conftest import user_token


class TestGetUserOrders:

    @allure.title('Получение пустого списка заказов авторизованного пользователя')
    def test_get_orders_empty_with_auth(self, user_token):
        response = ApiService.get_user_orders(token=user_token)
        assert (response.status_code == 200
                and response.json().get("success") is True
                and isinstance(response.json().get("orders"), list))

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_with_auth(self, user_token):
        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", '61c0c5a71d1f82001bdaaa73']
        ApiService.create_order(
            payload=PayloadBuilder.make_create_order_payload(ingredients),
            token=user_token
        )
        response = ApiService.get_user_orders(token=user_token)
        assert (response.status_code == 200
                and response.json().get("success") is True
                and response.json().get("orders")[0].get('ingredients') is not None)

    @allure.title('Попытка получения заказов неавторизованного пользователя')
    def test_get_orders_without_auth(self):
        response = ApiService.get_user_orders(token='')
        assert (response.status_code == 401
                and response.json() == ExpectedResponses.GET_USER_ORDERS_UNAUTHORIZED_RESPONSE)

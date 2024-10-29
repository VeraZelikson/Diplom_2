import pytest
import allure

from helpers.api_service import ApiService
from helpers.expected_responses import ExpectedResponses
from helpers.payload_builder import PayloadBuilder


class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_and_ingredients(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        access_token = ApiService._get_access_token(payload)

        ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", '61c0c5a71d1f82001bdaaa73']
        order_payload = PayloadBuilder.make_create_order_payload(ingredients)
        response = ApiService.create_order(order_payload, token=access_token)
        assert (response.status_code == 200
                and response.json().get("success") is True
                and "order" in response.json())

    @allure.title('Попытка создания заказа без авторизации')
    def test_create_order_without_auth(self):
        order_payload = PayloadBuilder.make_create_order_payload(["61c0c5a71d1f82001bdaaa6d"])
        response = ApiService.create_order(order_payload, token='')
        assert (response.status_code == 401
                and response.json() == ExpectedResponses.GET_USER_ORDERS_UNAUTHORIZED_RESPONSE)

    @allure.title('Попытка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        access_token = ApiService._get_access_token(payload)

        order_payload = PayloadBuilder.make_create_order_payload([])
        response = ApiService.create_order(order_payload, token=access_token)
        assert (response.status_code == 400
                and response.json() == ExpectedResponses.CREATE_ORDER_NO_INGREDIENTS_RESPONSE)

    @allure.title('Попытка создания заказа с невалидным хешем ингредиента')
    def test_create_order_with_invalid_ingredient_hash(self):
        payload = PayloadBuilder.make_user_create_payload()
        ApiService.create_user(payload)
        access_token = ApiService._get_access_token(payload)

        order_payload = PayloadBuilder.make_create_order_payload(["invalid_hash"])
        response = ApiService.create_order(order_payload, token=access_token)

        assert response.status_code == 500 and response.json() == ExpectedResponses.CREATE_ORDER_INVALID_HASH_RESPONSE

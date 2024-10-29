import allure
import requests

from helpers.payload_builder import PayloadBuilder
from helpers.urls import Urls


class ApiService:

    @staticmethod
    def _get_access_token(payload):
        return ApiService.login_user(
            PayloadBuilder.make_login_payload(
                email=payload['email'],
                password=payload['password']
            )
        ).json().get("accessToken")

    @staticmethod
    @allure.step('Создать юзера payload = {payload}')
    def create_user(payload=PayloadBuilder.make_user_create_payload()):
        return requests.post(url=Urls.USER_CREATING_URL, data=payload)

    @staticmethod
    @allure.step('Залогинить юзера payload = {payload}')
    def login_user(payload):
        return requests.post(url=Urls.USER_LOGIN_URL, data=payload)

    @staticmethod
    @allure.step('Обновление данных юзера payload = {payload}')
    def update_user(payload, token):
        return requests.patch(
            url=Urls.USER_CHANGE_URL,
            headers={
                'Authorization': token,
                'Content-Type': 'application/json'
            },
            json=payload
        )

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        return requests.delete(
            url=Urls.USER_CHANGE_URL,
            headers={
                'Authorization': token,
                'Content-Type': 'application/json'
            }
        )

    @staticmethod
    @allure.step('Создать заказ payload = {payload}')
    def create_order(payload, token):
        return requests.post(
            url=Urls.ORDERS_URL,
            headers={
                'Authorization': token,
                'Content-Type': 'application/json'
            },
            json=payload
        )

    @staticmethod
    @allure.step('Получить список доступных заказов юзера query = {query}')
    def order_list(query):
        return requests.get(url=Urls.ORDERS_URL, params=query)

    @staticmethod
    @allure.step('Получить заказы пользователя с авторизацией')
    def get_user_orders(token):
        return requests.get(url=Urls.ORDERS_URL, headers={'Authorization': token, 'Content-Type': 'application/json'})

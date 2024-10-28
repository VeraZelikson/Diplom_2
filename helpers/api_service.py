import allure
import requests

from helpers.payload_builder import PayloadBuilder
from helpers.urls import Urls


class ApiService:

    @staticmethod
    @allure.step('Создать юзера payload = {payload}')
    def create_user(payload=PayloadBuilder.make_user_create_payload()):
        return requests.post(url=Urls.USER_CREATING_URL, data=payload)

    @staticmethod
    @allure.step('Залогинить юзера payload = {payload}')
    def login_user(payload):
        return requests.post(url=Urls.USER_LOGIN_URL, data=payload)

    @staticmethod
    @allure.step('Создать заказ payload = {payload}')
    def create_order(payload):
        return requests.post(url=Urls.ORDERS_URL, data=payload)

    @staticmethod
    @allure.step('Получить список доступных заказов юзера query = {query}')
    def order_list(query):
        return requests.get(url=Urls.ORDERS_URL, params=query)
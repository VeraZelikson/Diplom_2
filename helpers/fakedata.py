import allure
from faker import Faker


class FakeData:
    @staticmethod
    @allure.step('Сгенирировать рандомный пароль длиной {length}')
    def generate_random_password(length):
        return Faker().password(length)

    @staticmethod
    @allure.step('Сгенирировать рандомное имя')
    def generate_random_name():
        return Faker().name()

    @staticmethod
    @allure.step('Сгенерировать рандомный email')
    def generate_random_email():
        return Faker().email()

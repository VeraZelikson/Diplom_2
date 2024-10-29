from helpers.fakedata import FakeData


class PayloadBuilder:
    @staticmethod
    def make_user_create_payload(with_email=True, with_password=True, with_name=True):
        payload = {}
        if with_email:
            payload["email"] = FakeData.generate_random_email()
        if with_password:
            payload["password"] = FakeData.generate_random_password(10)
        if with_name:
            payload["name"] = FakeData.generate_random_name()
        return payload

    @staticmethod
    def make_login_payload(email, password):
        payload = {}
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        return payload

    @staticmethod
    def make_create_order_payload(ingredients: list):
        return {'ingredients': ingredients}
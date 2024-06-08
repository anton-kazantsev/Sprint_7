import requests
import allure
from data_urls import DataUrls
from helpers import DataGeneration


class MethodsCourier:
    @staticmethod
    @allure.step('Создаем курьера')
    def create_courier(data_payload):
        response = requests.post(DataUrls.MAIN_URL + DataUrls.CREATE_COURIER, data=data_payload)
        return response

    @staticmethod
    @allure.step('Создаем курьера с данными созданного курьера')
    def duplicate_create_courier(data_payload):
        requests.post(DataUrls.MAIN_URL + DataUrls.CREATE_COURIER, data=data_payload)
        response_two = requests.post(DataUrls.MAIN_URL + DataUrls.CREATE_COURIER, data=data_payload)
        return response_two

    @staticmethod
    @allure.step('Создаем курьера с пустыми данными одного из обязательных полей')
    def not_once_required_field():
        data_login = DataGeneration.create_new_courier_and_return_login_password()["login"]
        data = {
            "login": data_login,
            "password": ""
        }
        response = requests.post(DataUrls.MAIN_URL + DataUrls.CREATE_COURIER, data=data)
        return response

    @staticmethod
    @allure.step('Вход курьера')
    def login_courier(data_payload):
        requests.post(DataUrls.MAIN_URL + DataUrls.CREATE_COURIER, data=data_payload)
        response = requests.post(DataUrls.MAIN_URL + DataUrls.LOGIN_COURIER, data=data_payload)
        return response

    @staticmethod
    @allure.step('Вход курьера с пустым полем Пароль')
    def login_courier_not_field_password():
        data_payload = DataGeneration.create_new_courier_and_return_login_password()
        data = {
            "login": data_payload["login"],
            "password": ""
        }
        response = requests.post(DataUrls.MAIN_URL + DataUrls.LOGIN_COURIER, data=data)
        return response

    @staticmethod
    @allure.step('Вход курьера с несуществующими данными')
    def courier_login_with_not_data():
        data_payload = DataGeneration.create_new_courier_and_return_login_password()
        response = requests.post(DataUrls.MAIN_URL + DataUrls.LOGIN_COURIER, data=data_payload)
        return response
import requests
import allure
from data_urls import DataUrls

class DataOrder:
    @staticmethod
    @allure.step('Создаем заказ')
    def creating_order(payload):
        response = requests.post(DataUrls.MAIN_URL + DataUrls.ORDER, data=payload)
        return response

    @staticmethod
    @allure.step('Получаем список заказов')
    def get_list_order():
        response = requests.get(DataUrls.MAIN_URL + DataUrls.ORDER)
        return response
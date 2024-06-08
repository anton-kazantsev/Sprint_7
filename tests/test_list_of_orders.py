import allure
from api.order_api import DataOrder


class TestGetListOfOrder:
    @allure.title('Проверка получения списка заказов')
    @allure.description(
        'Проверяем получение общего списка заказов, получаем статус 200 и проверяем, что список не пустой')
    def test_get_list_of_order(self):
        orders = DataOrder.get_list_order()
        assert orders.status_code == 200 and orders.json()["orders"] != []
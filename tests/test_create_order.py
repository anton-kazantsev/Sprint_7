import allure
import pytest
from data_user import DataCreatingOrder
from api.order_api import DataOrder


class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Создание заказа с различным выбором цвета самоката')
    @pytest.mark.parametrize(
        'payload',
        [
            DataCreatingOrder.create_data_for_order(["BLACK"]),
            DataCreatingOrder.create_data_for_order(["BLACK", "GREY"]),
            DataCreatingOrder.create_data_for_order([""])
        ]
    )
    def test_create_order(self, payload):
        order = DataOrder.creating_order(payload)
        assert order.status_code == 201 and order.json()['track'] != 0
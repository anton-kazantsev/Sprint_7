import allure
from api.courier_api import MethodsCourier
from data_answers import Answers
from conftest import create_and_delete_account_courier


class TestLoginCourier:
    @allure.title('Проверка успешного логина курьера')
    @allure.description(
        'Создаём аккаунт курьера и логинимся на него, получаем статус 200 и убеждаемся, что id приходит')
    def test_successful_courier_login(self, create_and_delete_account_courier):
        user = MethodsCourier.login_courier(create_and_delete_account_courier)
        assert user.status_code == 200 and user.json()['id'] != 0

    @allure.title('Проверка попытки логина курьера без поля password')
    @allure.description(
        'Пытаемся залогиниться на аккаунт без поля Пароль и получаем ошибку 400 и соответствующий текст ответа')
    def test_not_password_courier(self):
        user = MethodsCourier.login_courier_not_field_password()
        assert user.status_code == 400 and user.json()['message'] == Answers.NOT_ENOUGH_DATA_TO_LOG_IN

    @allure.title('Проверка логина несуществующим курьером')
    @allure.description(
        'Пытаемся залогиниться несуществующим аккаунтом курьера, получаем ошибку 404 и соответствующее сообщение')
    def test_no_such_username_and_password(self):
        user = MethodsCourier.courier_login_with_not_data()
        assert user.status_code == 404 and user.json()['message'] == Answers.ACCOUNT_NOT_FOUND
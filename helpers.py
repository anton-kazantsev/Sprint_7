class DataGeneration:
    @classmethod
    def create_new_courier_and_return_login_password(cls):
        # Данные курьера
        login = "courier_test777"
        password = "777"
        first_name = "uzuke"

        # Записываем данные курьера
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Возвращаем данные курьера
        return payload
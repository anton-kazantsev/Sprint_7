import json

static_courier = ['courier_test666', '666', 'test666']

class DataCreatingOrder:
    @staticmethod
    def create_data_for_order(color):
        payload = {
            "firstName": "ninja",
            "lastName": "saske",
            "address": "address111",
            "metroStation": 1,
            "phone": "+79998889988",
            "rentTime": 3,
            "deliveryDate": "2024-06-10",
            "color": color,
            "comment": "comment for courier",
        }

        return json.dumps(payload)
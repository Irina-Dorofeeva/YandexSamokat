# Ирина Дорофеева, 22-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.ORDERS, json=body)

def get_order(track_id):
    get_order_url = configuration.URL_SERVICE + configuration.ORDERS + "/track?t=" + str(track_id)
    response = requests.get(get_order_url)
    return response

def test_create_order_and_get_order_information():
    response = create_order(data.order_body)
    track_id = response.json()["track"]
    order_response = get_order(track_id)
    assert order_response.status_code == 200, "Ошибка: " + str(order_response.status_code)
   

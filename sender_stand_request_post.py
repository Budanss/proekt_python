import requests
import configuration
import data

# POST-запрос на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body);
print('NEW USER:')
print(response.json())
print(response.status_code)
print(response.json())

# Поиск наборов по продуктам
def post_products_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=body,
                         headers=data.headers)

response_products_kits = post_products_kits(data.product_ids);
print('PRODUCTS_KITS_RESPONSE:')
print(response_products_kits.status_code)
print(response_products_kits.json())
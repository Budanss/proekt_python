import configuration
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print('Статус код get_docs:', response.status_code)


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})

response_logs = get_logs()
print('Статус код get_logs:', response_logs.status_code)
print('Заголовки get_logs:', response_logs.headers)
print('URL get_logs:', response_logs.url)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response_users_table = get_users_table()
print('Статус код get_users_table:', response_users_table.status_code)
print(response_users_table.url)
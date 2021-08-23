import pytest
import allure

from requests import get


"""Тестирование API Connection Points"""


@allure.feature('API Connection Points')
@pytest.mark.parametrize("parameter_value", ['0', '1'])
def test_points_data_extended(url_api_connection_points, parameter_value):
    """Тестирование отработки ключа extended и отражения его в данных meta"""
    key = '?extended='
    url = url_api_connection_points + key + parameter_value
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key}, равен {parameter_value}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Сравнение результата в meta по параметру {key} с {parameter_value}')
    assert result.json()['meta']['query']['extended'] == parameter_value


@allure.feature('API Connection Points')
@pytest.mark.parametrize("key_name", ['isInterconnection', 'isPlanned'])
@pytest.mark.parametrize("parameter", ['0', '1'])
def test_points_data_ic_and_planned(url_api_connection_points, key_name, parameter):
    """Тестирование отработки ключей isInterconnection, isPlanned и корректного отражения его в данных"""
    url = f'{url_api_connection_points}?{key_name}={parameter}'
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key_name}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Обработка данных и подсчёт значений ключа {key_name}')
    values = set([x[key_name] for x in result.json()['connectionPoints']])
    check_value = bool(int(parameter))
    allure.step(f'Проверка того, что все точки имеют значение ключа {key_name} {check_value}')
    assert (len(values) == 1) & (check_value in values)


@allure.feature('API Connection Points')
@pytest.mark.parametrize("parameter", range(4))  # sample(range(10, 30), 4)
def test_points_data_limit(url_api_connection_points, parameter, random_number_upto_30):
    """Тестирование корректной отработки ключа limit"""
    parameter = random_number_upto_30[parameter]
    key = '?limit='
    url = url_api_connection_points + key + str(parameter)
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка соответствия количества данных {parameter}.')
    assert len(result.json()['connectionPoints']) == parameter


@allure.feature('API Connection Points')
@pytest.mark.parametrize("key_name", ['pointKey', 'pointLabel', 'pointType'])
@pytest.mark.parametrize("parameter", range(5))  # sample(range(99), 4)
def test_points_data_points_data(url_api_connection_points,
                                 connection_points_sample_data,
                                 key_name,
                                 parameter,
                                 random_number_upto_99):
    """Тестирование отработки ключей pointKey, pointLabel, pointType и корректного отражения его в данных"""
    parameter = random_number_upto_99[parameter]
    url = f'{url_api_connection_points}?{key_name}={connection_points_sample_data[parameter][key_name]}'
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key_name}, '
                         f'равен {connection_points_sample_data[parameter][key_name]}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Обработка данных и подсчёт значений ключа {key_name}')
    values = set([x[key_name] for x in result.json()['connectionPoints']])
    assert (len(values) == 1) & (connection_points_sample_data[parameter][key_name] in values)

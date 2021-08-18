from random import uniform

import pytest
from requests import get
import allure

"""Тестирование API Connection Points"""


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


@pytest.mark.parametrize("key_name", ['isInterconnection', 'isPlanned'])
@pytest.mark.parametrize("parameter", ['0', '1'])
def test_points_data_ic_and_planned(url_api_connection_points, key_name, parameter):
    """Тестирование отработки ключей isInterconnection, isPlanned и корректного отражения его в данных"""
    key = f'?{key_name}='
    url = url_api_connection_points + key + parameter
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Обработка данных и подсчёт значений ключа {key_name}')
    values = set([x[key_name] for x in result.json()['connectionPoints']])
    if parameter == '0':
        allure.step(f'Проверка того, что все точки имеют значение ключа {key} False')
        check_value = False
    else:
        allure.step(f'Проверка того, что все точки имеют значение ключа {key} True')
        check_value = True
    assert (len(values) == 1) & (check_value in values)


@pytest.mark.parametrize("parameter", [int(uniform(10, 30)) for x in range(3)])
def test_points_data_limit(url_api_connection_points, parameter):
    """Тестирование корректной отработки ключа limit"""
    key = '?limit='
    url = url_api_connection_points + key + str(parameter)
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка соответствия количества данных {parameter}.')
    assert len(result.json()['connectionPoints']) == parameter


@pytest.mark.parametrize("key_name", ['pointKey', 'pointLabel', 'pointType'])
@pytest.mark.parametrize("parameter", [int(uniform(0, 99)) for x in range(5)])
def test_points_data_points_data(url_api_connection_points, connection_points_sample_data, key_name, parameter):
    """Тестирование отработки ключей pointKey, pointLabel, pointType и корректного отражения его в данных"""
    key = f'?{key_name}='
    url = url_api_connection_points + key + connection_points_sample_data[parameter][key_name]
    print(url)
    allure.dynamic.title(f'Тестирование API: {url_api_connection_points}, параметр: {key_name}, '
                         f'равен {connection_points_sample_data[parameter][key_name]}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Обработка данных и подсчёт значений ключа {key_name}')
    values = set([x[key_name] for x in result.json()['connectionPoints']])
    assert (len(values) == 1) & (connection_points_sample_data[parameter][key_name] in values)

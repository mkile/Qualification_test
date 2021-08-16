from random import uniform

import pytest
from requests import get
import allure
from datetime import datetime, timedelta

"""Тестирование API Operational Data"""


@pytest.mark.parametrize("parameter_name", ['allIndicatorsChecked', 'nonIndicatorsChecked'])
@pytest.mark.parametrize("parameter_value", ['0', '1'])
def test_op_data_indicators_checked(url_api_operational_data, parameter_name, parameter_value):
    """Тестирование отработки ключей allIndicatorsChecked, nonIndicatorsChecked и отражения его в данных meta"""
    key = f'?{parameter_name}='
    url = url_api_operational_data + key + parameter_value
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {parameter_value}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Сравнение результата в meta по параметру {key} с {parameter_value}')
    assert result.json()['meta']['query'][parameter_name] == parameter_value


@pytest.mark.parametrize("indicator", ['Allocation', 'Firm Technical', 'GCV', 'Physical Flow'])
def test_op_data_indicators(url_api_operational_data, indicator):
    """Тестирование корректной отработки ключа indicator"""
    key = '?indicator='
    url = url_api_operational_data + key + indicator
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {indicator}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка отсутствия других индикаторов кроме {indicator} и наличия его самого.')
    indicators = set([x['indicator'] for x in result.json()['operationalData']])
    assert (len(indicators) == 1) & (indicator in indicators)


@pytest.mark.parametrize("indicator", ['Allocation', 'Firm Technical', 'GCV', 'Physical Flow'])
@pytest.mark.parametrize("parameter", [int(uniform(1, 30)) for x in range(1)])
def test_op_data_from(url_api_operational_data, indicator, parameter):
    """Тестирование корректной отработки ключа from и загрузки дат начиная с указанной для разных индикаторов"""
    key = f'?indicator={indicator}&from='
    date = datetime.strftime(datetime.today() - timedelta(days=parameter), '%Y-%m-%d')
    url = url_api_operational_data + key + date
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {date}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка отсутствия дат ранее {date}')
    dates = [x['periodFrom'][:10] for x in result.json()['operationalData']]
    assert min(dates) == date


@pytest.mark.parametrize("parameter", [int(uniform(10, 30)) for x in range(3)])
def test_op_data_limit(url_api_operational_data, parameter):
    """Тестирование корректной отработки ключа limit"""
    key = '?limit='
    url = url_api_operational_data + key + str(parameter)
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка соответствия количества данных {parameter}.')
    assert len(result.json()['operationalData']) == parameter


@pytest.mark.parametrize("parameter", ['hour', 'day'])
def test_op_data_periodtype(url_api_operational_data, parameter):
    """Тестирование отработки ключа periodType и корректного отражения его в данных"""
    key = '?periodType='
    url = url_api_operational_data + key + parameter
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка того, что все данные по ключу {key} равны {parameter}')
    periodtype = set([x['periodType'] for x in result.json()['operationalData']])
    assert (len(periodtype) == 1) & (parameter in periodtype)


@pytest.mark.parametrize("indicator", ['Allocation', 'Firm Technical', 'GCV', 'Physical Flow'])
@pytest.mark.parametrize("parameter", [int(uniform(2, 10)) for x in range(1)])
def test_op_data_to(url_api_operational_data, indicator, parameter):
    """Тестирование корректной отработки ключа to и загрузки дат заканчивая на указанной для разных индикаторов"""
    from_date = datetime.strftime(datetime.today() - timedelta(days=parameter * 2), '%Y-%m-%d')
    to_date = datetime.strftime(datetime.today() - timedelta(days=parameter), '%Y-%m-%d')
    key = f'?indicator={indicator}&from={from_date}&to='
    url = url_api_operational_data + key + to_date
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {to_date}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка отсутствия дат позднее {to_date}')
    dates = [x['periodFrom'][:10] for x in result.json()['operationalData']]
    assert max(dates) == to_date

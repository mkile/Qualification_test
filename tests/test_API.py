import pytest
from requests import get
import allure
from datetime import datetime, timedelta
import logging


@pytest.mark.parametrize("parameter", ['0', '1'])
def test_title_value(url_api_operational_data, parameter):
    """Тестирование отработки ключа allIndicatorsChecked и отражения его в данных meta"""
    key = '?allIndicatorsChecked='
    url = url_api_operational_data + key + parameter
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {parameter}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Сравнение результата в meta по параметру {key} с {parameter}')
    assert result.json()['meta']['query']['allIndicatorsChecked'] == parameter


@pytest.mark.parametrize("parameter", [5, 10])
def test_title_value(url_api_operational_data, parameter):
    """Тестирование корректной отработки ключа from и загрузки дат начиная с указанной"""
    key = '?indicator=GCV&from='
    date = datetime.strftime(datetime.today() - timedelta(days=parameter), '%Y-%m-%d')
    url = url_api_operational_data + key + date
    allure.dynamic.title(f'Тестирование API: {url_api_operational_data}, параметр: {key}, равен {date}')
    allure.step(f'Обращение по ссылке: {url}')
    result = get(url)
    allure.step(f'Проверка отсутствия дат ранее {date}')
    dates = [x['periodFrom'][:10] for x in result.json()['operationalData']]
    assert min(dates) == date

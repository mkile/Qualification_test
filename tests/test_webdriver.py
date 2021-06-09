import pytest
from re import match
import allure


def test_title_value(browser, url):
    allure.dynamic.title(f'Проверка работы браузера при открытии ссылки {url}')
    allure.step(f'Open {url}')
    browser.get(url)
    current_title = match(r'.+o|Opencart.+', browser.title)
    assert current_title

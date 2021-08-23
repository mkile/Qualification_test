import allure
from re import match


@allure.feature('Работа браузера')
def test_title_value(browser, url):
    """Проверка открытия базовой ссылки, чтобы понять работает ли webdriver"""
    allure.dynamic.title(f'Проверка работы браузера при открытии ссылки {url}')
    allure.step(f'Open {url}')
    browser.get(url)
    assert match(r'.+o|ENTSOG.+', browser.title)

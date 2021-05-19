import pytest
from selenium import webdriver
import json
import os

DRIVERS = './drivers/'


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     choices=['chrome', 'firefox', 'opera'],
                     default='chrome',
                     help='Укажите драйвер')
    parser.addoption('--url',
                     action='store',
                     default='https://demo.opencart.com',
                     help='Укажите ссылку на сайт Opencart')
    parser.addoption('--headless',
                     action='store_true',
                     default=False,
                     help='Запускать ли браузер в headless режиме')
    parser.addoption('--timeout',
                     action='store',
                     default=5,
                     type=int,
                     help='Время ожидания элемента на странице')


@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    timeout = request.config.getoption('--timeout')
    driver = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = request.config.getoption('--headless')
        driver = webdriver.Chrome(executable_path=DRIVERS + 'chromedriver.exe', options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = request.config.getoption('--headless')
        driver = webdriver.Firefox(executable_path=DRIVERS + 'geckodriver.exe', options=options)
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=DRIVERS + 'operadriver.exe')
    driver.timeout = timeout
    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture()
def url(request):
    url = request.config.getoption('--url')
    return url


@pytest.fixture(scope='module')
def test_parameters():
    with open(os.path.abspath('data/test_data.json'), 'r') as file:
        json_data = json.loads(file.read())
    yield json_data

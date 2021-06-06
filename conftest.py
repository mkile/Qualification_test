import pytest
from selenium import webdriver
import json
import os

DRIVERS = './drivers/'


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     choices=['chrome', 'firefox', 'opera'],
                     default='firefox',
                     help='Укажите драйвер')
    parser.addoption('--url',
                     action='store',
                     default='http://demo.opencart.com',
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
    parser.addoption('--oc_adm_name',
                     action='store',
                     default='demo',
                     type=str,
                     help='Логин от админки Opencart')
    parser.addoption('--oc_adm_pass',
                     action='store',
                     default='demo',
                     type=str,
                     help='Пароль от админки Opencart')
    parser.addoption("--selenoid", action="store_true", default=True)
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    timeout = request.config.getoption('--timeout')
    selenoid = request.config.getoption('--selenoid')
    executor = request.config.getoption('--executor')
    vnc = request.config.getoption('--vnc')
    videos = request.config.getoption('--videos')
    url = request.config.getoption('--url')
    driver = None
    if selenoid:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser,
            "name": "mkile",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )
    else:
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
    driver.get(url)

    return driver


@pytest.fixture(scope='module')
def test_parameters():
    with open(os.path.abspath('data/test_data.json'), 'r') as file:
        json_data = json.loads(file.read())
    yield json_data


@pytest.fixture(scope='module')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='module')
def admin_credentials(request):
    login = request.config.getoption('--oc_adm_name')
    password = request.config.getoption('--oc_adm_pass')
    return login, password


@pytest.fixture(scope='module')
def product_description():
    product_name = 'TestProduct'
    product_desc = 'TestDescription'
    product_meta = 'TestMeta'
    product_model = 'TestModel'
    return product_name, product_desc, product_meta, product_model


@pytest.fixture(scope='module')
def new_user_credentials():
    firstname = 'TestFirstName'
    lastname = 'TestLastName'
    email = 'test@test.ru'
    phone = '79415614565'
    password = '1234Strong_Pass'
    return firstname, lastname, email, phone, password

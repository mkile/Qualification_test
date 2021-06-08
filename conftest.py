import logging

import pytest
from selenium import webdriver
import json
import os

DRIVERS = './drivers/'

logging.basicConfig(level=logging.INFO, filename="logs/test.log")


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
    parser.addoption("--selenoid", action="store_false", default=True)
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):

    def finalizer():
        driver.quit()
        logger.info("===> Test {} finished".format(test_name))

    browser = request.config.getoption('--browser')
    timeout = request.config.getoption('--timeout')
    selenoid = request.config.getoption('--selenoid')
    executor = request.config.getoption('--executor')
    vnc = request.config.getoption('--vnc')
    videos = request.config.getoption('--videos')
    url = request.config.getoption('--url')
    driver = None
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))

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
        logger.info(f"Selenoid session starting with browser {browser}")
    else:
        logger.info(f"Local session starting with browser {browser}")
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
    request.addfinalizer(finalizer)
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


@pytest.fixture(autouse=True, scope="session")
def get_environment(pytestconfig, request):
    alluredir = request.config.getoption('--alluredir')
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/{alluredir}/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')


@pytest.fixture(autouse=True, scope="session")
def clean_allure_results_dir(request):
    logger = logging.getLogger('BrowserLogger')
    alluredir = request.config.getoption('--alluredir')
    for root, dirs, files in os.walk(alluredir):
        for filename in files:
            if filename != 'categories.json':
                os.remove(os.path.join(alluredir, filename))
    logger.info(f'Cleaned allure reports folder - {alluredir}')

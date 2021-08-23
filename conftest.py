import logging
import pytest
import os
import allure

from requests import get
from selenium import webdriver
from random import sample

logging.basicConfig(level=logging.INFO, filename="logs/test.log", format='[%(asctime)s] %(message)s')


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     choices=['chrome', 'firefox', 'opera'],
                     default='firefox',
                     help='Укажите драйвер')
    parser.addoption('--url',
                     action='store',
                     default='https://transparency.entsog.eu/',
                     help='Укажите ссылку на сайт ENTSOG')
    parser.addoption('--timeout',
                     action='store',
                     default=10,
                     type=int,
                     help='Время ожидания элемента на странице')
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--screenresolution", action="store", default="1920x1080x24")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def browser(request):
    def finalizer():
        # Finalizer with screenshot on error
        logger.info('Running browser Teardown')
        if request.node.rep_call.failed:
            logger.warning('Detected failed test, trying to add screenshot')
            # Make the screen-shot if test failed:
            try:
                driver.execute_script("document.body.bgColor = 'white';")

                allure.attach(driver.get_screenshot_as_png(),
                              name=request.function.__name__,
                              attachment_type=allure.attachment_type.PNG)
                logger.warning('Screenshot attached')
            except Exception as Err:
                logger.warning('Could not add screenshot')
        driver.quit()
        logger.info("===> Test {} finished".format(test_name))

    logger = logging.getLogger('BrowserLogger')
    # Read command line parameters
    browser = request.config.getoption('--browser')
    logger.info(f'Browser parameter ={browser}')
    timeout = request.config.getoption('--timeout')
    logger.info(f'Timeout parameter ={timeout}')
    executor = request.config.getoption('--executor')
    logger.info(f'Executor parameter ={executor}')
    vnc = request.config.getoption('--vnc')
    logger.info(f'VNC parameter ={vnc}')
    url = request.config.getoption('--url')
    logger.info(f'Url parameter ={url}')
    resolution = request.config.getoption('--screenresolution')
    logger.info(f'Resolution parameter ={resolution}')
    # Init logging and driver
    driver = None
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))

    executor_url = f"http://{executor}:4444/wd/hub"
    caps = {
        "browserName": browser,
        "screenResolution": resolution,
        "name": "mkile",
        "selenoid:options": {
            "enableVNC": vnc
        }
    }
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )
    logger.info(f"Selenoid session starting with browser {browser}")
    driver.timeout = timeout
    request.addfinalizer(finalizer)
    driver.get(url)
    driver.maximize_window()
    return driver


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def url_api_operational_data(request):
    return request.config.getoption('--url') + 'api/v1/operationalData'


@pytest.fixture(scope='session')
def url_api_connection_points(request):
    return request.config.getoption('--url') + 'api/v1/connectionPoints'


@pytest.fixture(scope='session')
def connection_points_sample_data(url_api_connection_points):
    data = get(url_api_connection_points)
    result = [{'pointKey': x['pointKey'],
               'pointLabel': x['pointLabel'],
               'pointType': x['pointType']} for x in data.json()['connectionPoints']]
    return result


@pytest.fixture(autouse=True, scope="session")
def get_environment(pytestconfig):
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')


@pytest.fixture()
def random_number_upto_10():
    return sample(range(1, 30), 10)


@pytest.fixture()
def random_number_upto_30():
    return sample(range(1, 30), 10)


@pytest.fixture()
def random_number_upto_99():
    return sample(range(99), 10)

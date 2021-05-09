import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

DELAY = 2


@pytest.mark.parametrize("page", range(5))
@pytest.mark.parametrize("element", range(5))
def test_admin_page_elements(browser, page, element, test_parameters, url):
    keys = list(test_parameters.keys())
    current_page = test_parameters[keys[page]]
    browser.get(url + keys[page])
    try:
        WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, current_page[element]))
        )
    except TimeoutException as Err:
        raise AssertionError("На странице {} не найден элемент {}".format(keys[page], current_page[element]))
    else:
        assert True
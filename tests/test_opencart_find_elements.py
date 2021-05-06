import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

DELAY = 2


@pytest.mark.parametrize("page", range(5))
@pytest.mark.parametrize("element", range(5))
def test_admin_page_elements(browser, page, element, test_parameters, url):
    keys = list(test_parameters.keys())
    current_page = test_parameters[keys[page]]
    browser.get(url + keys[page])
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, current_page[element]))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True

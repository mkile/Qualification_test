import pytest
from page_objects.GenericPage import GenericPage


@pytest.mark.parametrize("page", range(5))
@pytest.mark.parametrize("element", range(5))
def test_admin_page_elements(browser, page, element, test_parameters, url):
    keys = list(test_parameters.keys())
    current_page = test_parameters[keys[page]]
    browser.get(url + keys[page])
    GenericPage(browser).wait_element(current_page[element])

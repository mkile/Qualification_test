import pytest
from re import match


def test_title_value(browser, url):
    """
    Testing browser run functionality
    """
    browser.get(url)
    current_title = match(r'.+o|Opencart.+', browser.title)
    assert current_title

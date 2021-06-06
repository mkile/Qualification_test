import pytest
from re import match


def test_title(browser, url):
    """
    Testing browser run functionality
    :param browser:
    :param url:
    :return:
    """
    browser.get(url)
    current_title = match(r'.+o|Opencart.+', browser.title)
    assert current_title

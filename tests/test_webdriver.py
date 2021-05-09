import pytest
from re import match


def test_title(browser, url):
    browser.get(url)
    current_title = match(r'.+o|Opencart.+', browser.title)
    assert current_title

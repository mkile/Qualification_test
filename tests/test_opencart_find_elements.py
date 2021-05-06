import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

DELAY = 2


@pytest.mark.parametrize("element", ['#slideshow0',
                                     '#carousel0',
                                     '#menu',
                                     '#top-links',
                                     '#cart',
                                     '#search'])
def test_index_elements(browser, url, element):
    browser.get(url)
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True, element


@pytest.mark.parametrize("element", ['#top',
                                     '#menu',
                                     '.breadcrumb',
                                     '#column-left',
                                     '.swiper-viewport',
                                     '.product-thumb'])
def test_products_page_elements(browser, url, element):
    browser.get(url + '/index.php?route=product/category&path=20')
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True, element


@pytest.mark.parametrize("element", ['.thumbnails',
                                     '.image-additional',
                                     'button.btn-primary',
                                     'div.tab-content',
                                     'span.fa.fa-stack',
                                     'a.addthis_button_facebook_like'])
def test_product_page_elements(browser, url, element):
    browser.get(url + '/index.php?route=product/product&path=57&product_id=49')
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True, element


@pytest.mark.parametrize("element", ['a.btn.btn-primary',
                                     'input.btn.btn-primary',
                                     'label.control-label[for=input-email]',
                                     'label.control-label[for=input-password]',
                                     '#menu',
                                     '#cart'])
def test_login_page_elements(browser, url, element):
    browser.get(url + '/index.php?route=account/login')
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True, element


@pytest.mark.parametrize("element", ['h1.panel-title',
                                     '#input-username',
                                     '#input-password',
                                     'span.help-block',
                                     'button.btn-primary',
                                     '#header-logo'])
def test_admin_page_elements(browser, url, element):
    browser.get(url + '/admin')
    try:
        req_element = WebDriverWait(browser, DELAY).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except Exception as Err:
        req_element = False
    else:
        req_element = True
    assert req_element is True, element
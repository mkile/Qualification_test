import pytest
from page_objects.MainPage import MainPage
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from page_objects.AddProductPage import AddProductPage
import time


def test_add_new_product(browser, credentials, product_description):
    MainPage(browser).open_admin_login()
    AdminLoginPage(browser).login_with(*credentials)
    AdminPage(browser).open_products_page()
    AdminPage(browser).add_new_product_click()
    AddProductPage(browser).add_test_product(*product_description)
    time.sleep(3)
    AdminPage(browser).check_test_product_present(*product_description)
    time.sleep(3)
    AdminPage(browser).delete_test_product()
    time.sleep(3)

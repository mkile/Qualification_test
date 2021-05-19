from selenium.webdriver.common.by import By
from .BasePage import BasePage


class GenericPage(BasePage):

    def wait_element(self, element):
        self._verify_element_presence((By.CSS_SELECTOR, element))

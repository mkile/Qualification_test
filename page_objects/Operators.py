from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Operators(BasePage):
    OPERATORS_TABLE_SELECTOR = (By.CSS_SELECTOR, "table.list-operator")

    def operators_table_check(self):
        self._verify_element_presence(self.OPERATORS_TABLE_SELECTOR)

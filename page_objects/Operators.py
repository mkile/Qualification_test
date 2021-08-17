from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class Operators(BasePage):
    OPERATORS_FILTER_SORT_SELECTOR = (By.CSS_SELECTOR, "div.filter-sort")
    OPERATORS_TABLE_SELECTOR = (By.CSS_SELECTOR, "ul.list-operator")

    def operators_filter_sort_check(self):
        self._verify_element_presence(self.OPERATORS_FILTER_SORT_SELECTOR)

    def operators_table_check(self):
        self._verify_element_presence(self.OPERATORS_TABLE_SELECTOR)

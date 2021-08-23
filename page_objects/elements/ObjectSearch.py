from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ObjectSearch(BasePage):
    SEARCH_LINE_SELECTOR = (By.CSS_SELECTOR, 'input.form-control.search-field')

    def input_object_name(self, object_name):
        self._clear_and_send_keys(self.SEARCH_LINE_SELECTOR, object_name)

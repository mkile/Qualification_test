from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class PUInterruptions(BasePage):
    INTERRUPTIONS_TABLE_SELECTOR = (By.CSS_SELECTOR, "table.dataTable")
    INTERRUPTIONS_OPTION_SELECTOR = (By.CSS_SELECTOR, "div.calendar-option.interruption-col-side")

    def table_check(self):
        self._verify_element_presence(self.INTERRUPTIONS_TABLE_SELECTOR)

    def option_check(self):
        self._verify_element_presence(self.INTERRUPTIONS_OPTION_SELECTOR)

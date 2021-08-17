from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class PointsAdvancedSearch(BasePage):
    TABLE_SELECTOR = (By.CSS_SELECTOR, "table#points-search")

    def data_table_check(self):
        self._verify_element_presence(self.TABLE_SELECTOR)

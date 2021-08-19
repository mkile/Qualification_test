from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class PointsData(BasePage):
    NAVBAR_SELECTOR = (By.CSS_SELECTOR, "ul.nav.nav-tabs#tab-data")
    GRAPH_SELECTOR = (By.CSS_SELECTOR, "div.point-data-content")
    SIDE_PANEL_SELECTOR = (By.CSS_SELECTOR, "div.point-data-content")
    SIDE_CHART_RANGE_SELECTOR = (By.CSS_SELECTOR, "div.chart-range")
    SIDE_INDICATORS_SELECTOR = (By.CSS_SELECTOR, "div.point-indicator")

    def navbar_check(self):
        self._verify_element_presence(self.NAVBAR_SELECTOR)

    def data_graph_check(self):
        self._verify_element_presence(self.GRAPH_SELECTOR)

    def data_side_panel_check(self):
        self._verify_element_presence(self.GRAPH_SELECTOR)

    def data_side_panel_chart_range_check(self):
        self._verify_element_presence(self.SIDE_CHART_RANGE_SELECTOR)

    def data_side_panel_indicators_check(self):
        self._verify_element_presence(self.SIDE_INDICATORS_SELECTOR)

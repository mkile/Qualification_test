from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class UMMUnavailabilities(BasePage):
    UMM_UNAVAIL_TOOLBAR_SELECTOR = (By.CSS_SELECTOR, "ul.nav.nav-tabs#tab-data")
    UMM_UNAVAIL_CALENDAR_SELECTOR = (By.CSS_SELECTOR, "div.tab-pane.active#pane-gasFacilities")
    UMM_UNAVAIL_SIDEBAR_SELECTOR = (By.CSS_SELECTOR, "div.col-md-2")

    def navbar_check(self):
        self._verify_element_presence(self.UMM_UNAVAIL_TOOLBAR_SELECTOR)

    def calendar_check(self):
        self._verify_element_presence(self.UMM_UNAVAIL_CALENDAR_SELECTOR)

    def sidebar_check(self):
        self._verify_element_presence(self.UMM_UNAVAIL_SIDEBAR_SELECTOR)

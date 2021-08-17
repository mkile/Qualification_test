from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class UMMOtherMarketInformation(BasePage):
    UMM_OMM_TOOLBAR_SELECTOR = (By.CSS_SELECTOR, "ul.nav.nav-tabs#tab-data")
    UMM_OMM_TABLE_SELECTOR = (By.CSS_SELECTOR, "div.tab-pane.active#pane-otherMarkets")
    UMM_OMM_SIDEBAR_SELECTOR = (By.CSS_SELECTOR, "div.col-md-2")

    def navbar_check(self):
        self._verify_element_presence(self.UMM_OMM_TOOLBAR_SELECTOR)

    def table_check(self):
        self._verify_element_presence(self.UMM_OMM_TABLE_SELECTOR)

    def sidebar_check(self):
        self._verify_element_presence(self.UMM_OMM_SIDEBAR_SELECTOR)

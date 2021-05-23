from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    CATEGORY_PAGE_LI_SELECTOR = (By.CSS_SELECTOR,
                                 "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1) > a")
    CATEGORY_PAGE_LINK_SELECTOR = (By.CSS_SELECTOR,
                                   "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > "
                                   "ul > li:nth-child(1) > div > a")
    TABLET_CATEGORY_NAME = (By.CSS_SELECTOR,
                            "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(4) > a")
    USER_LOGIN_DROPDOWN_NAME = (By.CSS_SELECTOR,
                                "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md")
    USER_LOGIN_LINK_NAME = (By.CSS_SELECTOR,
                            "#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a")
    ADMIN_PAGE = '/admin/'

    def wait_element(self, element):
        self._verify_element_presence((By.CSS_SELECTOR, element))

    def open_category(self):
        element = self._verify_element_presence(self.CATEGORY_PAGE_LI_SELECTOR)
        self._click_element(element)
        element = self._verify_element_presence(self.CATEGORY_PAGE_LINK_SELECTOR)
        self._click_element(element)

    def open_tablet_category(self):
        element = self._verify_element_presence(self.TABLET_CATEGORY_NAME)
        self._click_element(element)

    def open_user_login(self):
        element = self._verify_element_presence(self.USER_LOGIN_DROPDOWN_NAME)
        self._click_element(element)
        element = self._verify_element_presence(self.USER_LOGIN_LINK_NAME)
        self._click_element(element)

    def open_admin_login(self):
        self.browser.get(self.browser.current_url + self.ADMIN_PAGE)

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    # points selectors
    POINTS_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'li.dropdown.points')
    POINTS_DROPDOWN_SELECTORS = (By.CSS_SELECTOR, 'li.dropdown.points > ul.dropdown-menu > li > a')
    # zones selectors
    ZONES_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'li.dropdown.zones > a')
    ZONES_DROPDOWN_SELECTORS = (By.CSS_SELECTOR, 'li.dropdown.zones > ul.dropdown-menu > li > a')
    # Calendar selectors
    CALENDAR_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'li.dropdown.calendar')
    CALENDAR_DROPDOWN_SELECTORS = (By.CSS_SELECTOR, 'li.dropdown.calendar > ul.dropdown-menu > li > a')
    # UMM selectors
    UMM_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'li.dropdown.umm')
    UMM_DROPDOWN_SELECTORS = (By.CSS_SELECTOR, 'li.dropdown.umm > ul.dropdown-menu > li > a')
    # Operators selector
    OPERATORS_SELECTOR = (By.CSS_SELECTOR, 'li.operators > a > span')
    # Map selectors
    MAP_POINTS_SELECTOR = (By.CSS_SELECTOR, 'div.map-marker-cb_itp_import-small')
    MAP_ZONES_SELECTOR = (By.CSS_SELECTOR, 'div.map-marker-balancing-zone-small')

    def wait_element(self, element):
        self._verify_element_presence((By.CSS_SELECTOR, element))

    def open_main_page(self):
        self._open_link(self.browser.current_url)

    def open_points_category(self):
        element = self._verify_element_presence(self.POINTS_DROPDOWN_SELECTOR)
        self._click_element(element)

    def open_points_map(self):
        self._verify_element_presence(self.POINTS_DROPDOWN_SELECTORS)
        elements = self._get_elements_children(self.POINTS_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Map').click()

    def open_points_advanced_search(self):
        self._verify_element_presence(self.POINTS_DROPDOWN_SELECTORS)
        elements = self._get_elements_children(self.POINTS_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Advanced search').click()

    def open_points_data(self):
        self._verify_element_presence(self.POINTS_DROPDOWN_SELECTORS)
        elements = self._get_elements_children(self.POINTS_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Data').click()

    def open_zones_category(self):
        element = self._verify_element_presence(self.ZONES_DROPDOWN_SELECTOR)
        self._click_element(element)

    def open_zones_map(self):
        self._verify_element_presence(self.ZONES_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.ZONES_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Map').click()

    def open_zones_advanced_search(self):
        self._verify_element_presence(self.ZONES_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.ZONES_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Advanced search').click()

    def open_zones_data(self):
        self._verify_element_presence(self.ZONES_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.ZONES_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Data').click()

    def open_operators(self):
        element = self._verify_element_presence(self.OPERATORS_SELECTOR)
        self._click_element(element)

    def open_calendar_category(self):
        element = self._verify_element_presence(self.CALENDAR_DROPDOWN_SELECTOR)
        self._click_element(element)

    def open_calendar_calendar_view(self):
        self._verify_element_presence(self.CALENDAR_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.CALENDAR_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Calendar view').click()

    def open_calendar_actual_unplanned_interruptions(self):
        self._verify_element_presence(self.CALENDAR_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.CALENDAR_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Actual/Unplanned Interruptions').click()

    def get_elements_by_id(self):
        self._verify_element_presence(self.POINTS_DROPDOWN_SELECTORS)
        elements = self._get_elements_children(self.POINTS_DROPDOWN_SELECTORS)
        self._click_element(elements(0))



    def open_umm_category(self):
        element = self._verify_element_presence(self.UMM_DROPDOWN_SELECTOR)
        self._click_element(element)

    # def open_user_login(self):
    #     element = self._verify_element_presence(self.USER_LOGIN_DROPDOWN_NAME)
    #     self._click_element(element)
    #     element = self._verify_element_presence(self.USER_LOGIN_LINKS)
    #     element = element.find_elements_by_css_selector("a")
    #     self._click_element(element[1])
    #
    # def open_user_register(self):
    #     element = self._verify_element_presence(self.USER_LOGIN_DROPDOWN_NAME)
    #     self._click_element(element)
    #     element = self._verify_element_presence(self.USER_LOGIN_LINKS)
    #     element = element.find_elements_by_css_selector("a")
    #     self._click_element(element[0])
    #
    # def open_admin_login(self):
    #     self._open_link(self.browser.current_url + self.ADMIN_PAGE)
    #
    # def switch_currency(self, currency):
    #     element = self._verify_element_presence(self.CURRENCY_DROPDOWN_NAME)
    #     self._click_element(element)
    #     element = self._verify_element_presence(self.CURRENCYS_LINKS)
    #     element = element.find_elements_by_css_selector("button")
    #     self._click_element(element[currency])

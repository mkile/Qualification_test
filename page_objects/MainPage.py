from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.elements.ObjectSearch import ObjectSearch


class MainPage(BasePage):
    # points selectors
    POINTS_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'li.dropdown.points > a.dropdown-toggle')
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
    MAP_PH_POINTS_SELECTOR = (By.CSS_SELECTOR, '#map > div.leaflet-map-pane > div.leaflet-objects-pane > '
                                               'div.leaflet-marker-pane > div.map-marker-physical')
    MAP_ZONES_SELECTOR = (By.CSS_SELECTOR, 'div.map-marker-balancing-zone-small')
    MAP_Z_POINTS_SELECTOR = (By.CSS_SELECTOR, '#map > div.leaflet-map-pane > div.leaflet-objects-pane > '
                                              'div.leaflet-marker-pane > div.map-marker-balancing-zone-small')
    MAP_PH_POINTS_SMALL_SELECTOR = (By.CSS_SELECTOR, 'div.map-marker-big')
    # search point scenario selectors
    FOUND_ELEMENT_SELECTOR = (By.CSS_SELECTOR,
                              'div.panel-group.list-points > div > div > div > h4[data-toggle="tooltip"]')
    ACCESS_DATA_SELECTOR = (By.CSS_SELECTOR, 'div.panel-group.list-points > div > div > div.connexion-bz.clearfix > '
                                             'div.rightPart > a.pointer.action.data')
    # map control elements
    ZOOM_IN_SELECTOR = (By.CSS_SELECTOR, 'a#zin')
    FILTER_PANEL_SELECTOR = (By.CSS_SELECTOR, 'div.rightPanel > div > a.filter.active')
    POINTS_FILTER_DROPDOWN_SELECTOR = (By.CSS_SELECTOR, 'ul.list-display > li > div > select')
    POINTS_FILTER_TEMPLATE = 'ul.list-display > li > div > select > option[value="{}"]'

    def wait_element(self, element):
        self._verify_element_presence((By.CSS_SELECTOR, element))

    def open_main_page(self):
        self._open_link(self.browser.current_url)

    def open_points_category(self):
        element = self._verify_element_presence(self.POINTS_DROPDOWN_SELECTOR)
        self._simple_click_element(element)

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

    def open_umm_category(self):
        element = self._verify_element_presence(self.UMM_DROPDOWN_SELECTOR)
        self._click_element(element)

    def open_umm_unavailabilities(self):
        self._verify_element_presence(self.UMM_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.UMM_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Unavailabilities of gas facilities').click()

    def open_umm_other_market_info(self):
        self._verify_element_presence(self.UMM_DROPDOWN_SELECTOR)
        elements = self._get_elements_children(self.UMM_DROPDOWN_SELECTORS)
        self._find_element_by_text(elements, 'Other Market Information').click()

    def get_elements_by_id(self):
        self._verify_element_presence(self.POINTS_DROPDOWN_SELECTORS)
        elements = self._get_elements_children(self.POINTS_DROPDOWN_SELECTORS)
        self._click_element(elements[0])

    def enter_object_name(self, object_name):
        ObjectSearch(self.browser).input_object_name(object_name)

    def open_found_points_dropdown(self):
        self._verify_element_presence(self.FOUND_ELEMENT_SELECTOR)
        elements = self._get_elements_children(self.FOUND_ELEMENT_SELECTOR)
        self._click_element(elements[0])

    def access_first_point_data_page(self):
        self._verify_element_presence(self.ACCESS_DATA_SELECTOR)
        elements = self._get_elements_children(self.ACCESS_DATA_SELECTOR)
        self._click_element(elements[0])

    def check_points_is_on_map(self):
        self._verify_element_presence(self.MAP_PH_POINTS_SELECTOR)

    def check_zones_not_on_map(self):
        self._check_element_absence(self.MAP_Z_POINTS_SELECTOR)

    def check_zones_is_on_map(self):
        self._verify_element_presence(self.MAP_Z_POINTS_SELECTOR)

    def check_points_not_on_map(self):
        self._check_element_absence(self.MAP_PH_POINTS_SELECTOR)

    def click_zoom_in(self):
        # time.sleep(10)
        element = self._verify_element_presence(self.ZOOM_IN_SELECTOR)
        # time.sleep(10)
        self._click_element(element)

    def big_small_point_on_the_map(self):
        self._verify_element_presence(self.MAP_PH_POINTS_SMALL_SELECTOR)

    def click_filter_panel(self):
        element = self._verify_element_presence(self.FILTER_PANEL_SELECTOR)
        self._simple_click_element(element)

    def filter_map_points(self, option):
        element = self._verify_element_presence((By.CSS_SELECTOR, self.POINTS_FILTER_TEMPLATE.format(option)))
        self._simple_click_element(element)

    def check_point_type_on_the_map(self, point_type):
        self._verify_element_presence((By.CSS_SELECTOR, point_type))

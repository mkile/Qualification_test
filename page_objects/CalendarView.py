from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CalendarView(BasePage):
    CALENDAR_SELECTOR = (By.CSS_SELECTOR, "div.calendar")
    CALENDAR_OPTION_SELECTOR = (By.CSS_SELECTOR, "div.calendar-option")

    def calendar_check(self):
        self._verify_element_presence(self.CALENDAR_SELECTOR)

    def calendar_option_check(self):
        self._verify_element_presence(self.CALENDAR_OPTION_SELECTOR)

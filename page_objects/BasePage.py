from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def _verify_link_presence(self, link_text):
        self.logger.info(f"Checking link: '{link_text}' presence...")
        try:
            return WebDriverWait(self.browser, self.browser.timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.logger.error('Link search timeout error.')
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        self.logger.info(f"Checking web element: '{locator}' presence...")
        try:
            return WebDriverWait(self.browser, self.browser.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error('Element search timeout error.')
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        self.logger.info(f"Running action chain to click element: '{element}' ...")
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        self.logger.info(f"Simple web element : '{locator}' click")
        element.click()

    def _click(self, locator: tuple):
        self.logger.info(f"Clicking web element: '{locator}'...")
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _clear_and_send_keys(self, locator, value):
        self.logger.info(f"Sending to: '{locator}' keys {value}.")
        self._element(locator).clear()
        self._element(locator).send_keys(value)

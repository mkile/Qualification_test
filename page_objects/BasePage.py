import logging
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Checking link presence.")
    def _verify_link_presence(self, link_text):
        self.logger.info(f"Checking link: '{link_text}' presence...")
        try:
            self.logger.info(f"Link found")
            return WebDriverWait(self.browser, self.browser.timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            self.logger.error('Link search timeout error.')
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    @allure.step("Checking web element presence.")
    def _verify_element_presence(self, locator: tuple):
        self.logger.info(f"Checking web element: '{locator}' presence...")
        try:
            element = WebDriverWait(self.browser, self.browser.timeout).until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element found")
            return element
        except TimeoutException:
            self.logger.error('Element search timeout error.')
            self.logger.error('Trying to attach screenshot.')
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f'screenshot-fail-to-find-{locator[1]}',
                          attachment_type=allure.attachment_type.PNG)
            self.logger.warning('Screenshot attached')
            self.logger.error('Trying to attach page source.')
            allure.attach(self.browser.page_source,
                          name=f'page_source-fail-to-find-{locator[1]}',
                          attachment_type=allure.attachment_type.TEXT)
            self.logger.warning('Source attached')
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Getting list of elements children.")
    def _get_elements_children(self, locator: tuple):
        self.logger.info(f"Getting list of elements: '{locator}' children...")
        try:
            elements = WebDriverWait(self.browser,
                                     self.browser.timeout).until(EC.visibility_of_any_elements_located(locator))
            self.logger.info(f"Number of elements found {len(elements)}")
            return elements
        except TimeoutException:
            self.logger.error('Elements search error.')
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    @allure.step("Running action chain to click element.")
    def _click_element(self, element):
        self.logger.info(f"Running action chain to click element: '{element}' ...")
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step("Simple web element click")
    def _simple_click_element(self, element):
        self.logger.info(f"Simple web element: '{element}' click")
        try:
            element.click()
        except AttributeError as Err:
            self.logger.error(f'Element {element} click error.')
            raise AssertionError("Cant click element. Error {}".format(Err))

    @allure.step("Move cursor to element")
    def _move_to_element(self, element):
        self.logger.info(f"Move cursor to element : '{element}'")
        ActionChains(self.browser).move_to_element(element)

    @allure.step("Clicking web element.")
    def _click(self, locator: tuple):
        self.logger.info(f"Clicking web element: '{locator}'...")
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step("Sending keys to input field.")
    def _clear_and_send_keys(self, locator, value):
        self.logger.info(f"Sending to: '{locator}' keys {value}.")
        self._element(locator).clear()
        self._element(locator).send_keys(value)

    @allure.step("Opening link.")
    def _open_link(self, url):
        self.logger.info(f"Opening link {url} ...")
        self.browser.get(url)

    @allure.step("Finding element in list by text.")
    def _find_element_by_text(self, elements, text):
        self.logger.info(f"Finding element by text: {text}")
        for element in elements:
            if element.text == text:
                return element
        self.logger.info(f"Element with text {text} not found.")
        raise AssertionError(f"Cant find element by text: {text}")

    @allure.step("Checking if element is not present.")
    def _check_element_absence(self, locator):
        self.logger.info(f"Checking if element is absent : {locator}")
        try:
            WebDriverWait(self.browser, self.browser.timeout).until(EC.visibility_of_any_elements_located(locator))
            raise AssertionError('Element found but it should not be')
        except TimeoutException:
            self.logger.info(f"Success: Element is not found")

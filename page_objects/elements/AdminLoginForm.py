from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class AdminLoginForm(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")

    def login_with(self, username, password):
        self._element(self.INPUT_EMAIL).clear()
        self._element(self.INPUT_EMAIL).send_keys(username)
        self._element(self.INPUT_PASSWORD).clear()
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.LOGIN_BUTTON).click()

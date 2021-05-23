from selenium.webdriver.common.by import By

from ..BasePage import BasePage


class ProductAddForm(BasePage):
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name1.form-control")
    INPUT_DESCRIPTION = (By.CSS_SELECTOR, "div.note-editable.panel-body")
    INPUT_META = (By.CSS_SELECTOR, "input#input-meta-title1")
    INPUT_MODEL = (By.CSS_SELECTOR, "input#input-model")

    def enter_general_parameters(self, product_name, product_desc, product_meta):
        self._element(self.INPUT_PRODUCT_NAME).clear()
        self._element(self.INPUT_PRODUCT_NAME).send_keys(product_name)
        self._element(self.INPUT_DESCRIPTION).click()
        self._element(self.INPUT_DESCRIPTION).send_keys(product_desc)
        self._element(self.INPUT_META).clear()
        self._element(self.INPUT_META).send_keys(product_meta)

    def enter_model(self, product_model):
        self._element(self.INPUT_MODEL).clear()
        self._element(self.INPUT_MODEL).send_keys(product_model)

from page_objects.MainPage import MainPage
from page_objects.elements.ObjectSearch import AdminLoginForm


class AdminLoginPage(MainPage):
    def login_with(self, username, password):
        AdminLoginForm(self.browser).login_with(username, password)

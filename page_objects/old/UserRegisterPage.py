from page_objects.MainPage import MainPage
from page_objects.old.elements.UserRegisterForm import UserRegisterForm


class UserRegisterPage(MainPage):

    def add_new_user(self, params: tuple):
        UserRegisterForm(self.browser).login_with(*params)

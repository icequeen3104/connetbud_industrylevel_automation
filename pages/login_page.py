from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config.env import BASE_URL


class LoginPage(BasePage):

    def open_application(self):
        self.navigate(BASE_URL)

    def click_parent_login(self):
        self.click(LoginLocators.PARENT_LOGIN_BUTTON)

    def enter_email(self, email):
        self.fill(LoginLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.fill(LoginLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login_to_application(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
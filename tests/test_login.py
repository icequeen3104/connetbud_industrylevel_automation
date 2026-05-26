from pages.login_page import LoginPage
from config.test_data_input import *

def test_01_verifying_login(page):
    '''Steps to verify login page
    1. Navigating to the website
    2. Clicking on parent login modal
    3. Inputting the login credentials
    4. Clicking on submit button
Expected results: The page will login and redirect to the home page
'''
    login_page = LoginPage(page)
    login_page.open_application()
    login_page.click_parent_login()
    login_page.login_to_application(LOGIN_EMAIL, LOGIN_PASSWORD)


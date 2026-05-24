import pytest

from pages.login_page import LoginPage

from config.test_data_input import *

@pytest.fixture
def login(page):

    login_page = LoginPage(page)

    login_page.open_application()

    login_page.click_parent_login()

    login_page.login_to_application(
        LOGIN_EMAIL,
        LOGIN_PASSWORD
    )

    return page
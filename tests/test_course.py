from pages.course_page import CoursePage
from config.test_data_input import *
from pages.login_page import LoginPage


def test_02_validating_course_selection(page):
    '''Steps to select a course
        1. After login, home page UI will be opened
        2. Select "languages" modal
        3. Then opt for the "english" course
        4. After which select a tutor by filtering
        5. Now hire the tutor
        6. Then select the number of classes to book
        7. Click on confirm button
        Expected results: Course will be booked and u will be redirected to the payment page
    '''
    login_page = LoginPage(page)
    login_page.open_application()
    login_page.click_parent_login()
    login_page.login_to_application(LOGIN_EMAIL, LOGIN_PASSWORD)

    course_page = CoursePage(page)
    course_page.complete_course_booking(NUMBER_OF_CLASSES)
from pages.course_page import CoursePage
from pages.booking_page import BookingPage
from config.test_data_input import *


def test_03_complete_booking_flow(login):

    page = login
    course_page = CoursePage(page)
    course_page.complete_course_booking(NUMBER_OF_CLASSES)


    booking_page = BookingPage(page)

    booking_page.complete_payment(
        CARD_NUMBER,
        EXPIRY_DATE,
        CARD_CVC,
        CARD_HOLDER_NAME,
        ADDRESS,
        CITY,
        PINCODE,
        STATE
    )

    booking_page.verify_url_page()

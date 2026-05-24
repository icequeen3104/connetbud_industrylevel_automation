from pages.base_page import BasePage

from locators.booking_locators import BookingLocators


class BookingPage(BasePage):

    def select_credit_card_option(self):
        self.click(BookingLocators.CREDIT_CARD_OPTION)

    def enter_card_number(self, card_number):
        self.fill(BookingLocators.CARD_NUMBER_INPUT, card_number)

    def enter_expiry_date(self, expiry):
        self.fill(BookingLocators.EXPIRY_DATE_INPUT, expiry)

    def enter_cvc(self, cvc):
        self.fill(BookingLocators.CVC_INPUT, cvc)

    def enter_card_holder_name(self, name):
        self.fill(BookingLocators.CARD_HOLDER_INPUT, name)

    def enter_manual_address(self):
        self.click(BookingLocators.ENTER_ADDRESS_MANUALLY)

    def enter_address(self, address):
        self.fill(BookingLocators.ADDRESS_INPUT, address)

    def enter_city(self, city):
        self.fill(BookingLocators.CITY_INPUT, city)

    def enter_pincode(self, pincode):
        self.fill(BookingLocators.PINCODE_INPUT, pincode)

    def select_state(self, state):
        self.select_dropdown(
            BookingLocators.STATE_DROPDOWN,
            state
        )

    def click_pay_button(self):
        self.click(BookingLocators.PAY_BUTTON)

    def complete_payment(
            self,
            card_number,
            expiry,
            cvc,
            name,
            address,
            city,
            pincode,
            state
    ):

        self.select_credit_card_option()

        self.enter_card_number(card_number)

        self.enter_expiry_date(expiry)

        self.enter_cvc(cvc)

        self.enter_card_holder_name(name)

        self.enter_manual_address()

        self.enter_address(address)

        self.enter_city(city)

        self.enter_pincode(pincode)

        self.select_state(state)

        self.click_pay_button()
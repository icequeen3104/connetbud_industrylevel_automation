class BookingLocators:

    CREDIT_CARD_OPTION = "//i[text()='Credit Card']"
    PAYMENT_METHOD_TEXT = "//h2[text()='Payment method']"
    CARD_NUMBER_INPUT = "//input[@id='cardNumber']"
    EXPIRY_DATE_INPUT = "//input[@placeholder='MM / YY']"
    CVC_INPUT = "//input[@id='cardCvc']"
    CARD_HOLDER_INPUT = "//input[@placeholder='Full name on card']"
    ENTER_ADDRESS_MANUALLY = "//span[text()='Enter address manually']"
    ADDRESS_INPUT = "//input[@id='billingAddressLine1']"
    CITY_INPUT = "//input[@placeholder='City']"
    PINCODE_INPUT = "//input[@placeholder='PIN']"
    STATE_DROPDOWN = "#billingAdministrativeArea"
    PAY_BUTTON = "[data-testid='hosted-payment-submit-button']"
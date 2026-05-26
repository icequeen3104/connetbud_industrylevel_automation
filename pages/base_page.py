from playwright.sync_api import expect

class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def click(self, locator):
        self.wait_for_element(locator)
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.wait_for_element(locator)
        self.page.locator(locator).fill(value)

    def wait_for_element(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_element_for_payment(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=60000)

    def select_dropdown(self, locator, value):
        self.page.locator(locator).select_option(label=value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def verify_url(self, expected_url):
        expect(self.page).to_have_url(expected_url, timeout=90000)
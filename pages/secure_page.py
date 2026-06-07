from playwright.sync_api import expect


class SecurePage:
    def __init__(self, page):
        self.page = page
        self.flash_message = page.locator("#flash")
        self.logout_button = page.locator("a.button.secondary.radius")

    def logout(self):
        self.logout_button.click()

    def expect_secure_page_loaded(self):
        expect(self.page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(self.flash_message).to_contain_text("You logged into a secure area!")
        expect(self.logout_button).to_be_visible()

    def expect_logout_button_visible(self):
        expect(self.logout_button).to_be_visible()

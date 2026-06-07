from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')
        self.flash_message = page.locator("#flash")

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_as_valid_user(self):
        self.login("tomsmith", "SuperSecretPassword!")

    def login_and_verify_success(self):
        self.expect_login_page_loaded()
        self.login_as_valid_user()

        from pages.secure_page import SecurePage
        secure_page = SecurePage(self.page)
        secure_page.expect_secure_page_loaded()

        return secure_page

    def expect_login_page_loaded(self):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_enabled()

    def expect_error_message(self, expected_text):
        expect(self.flash_message).to_contain_text(expected_text)

    def expect_logout_success(self):
        expect(self.flash_message).to_contain_text("You logged out of the secure area!")

    

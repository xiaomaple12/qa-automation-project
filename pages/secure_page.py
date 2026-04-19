class SecurePage:
    def __init__(self, page):
        self.page = page

    def get_flash_message(self):
        return self.page.locator("#flash").text_content()

    def logout(self):
        self.page.click("a.button.secondary.radius")

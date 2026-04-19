class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click('button[type="submit"]')

    def get_page_text(self):
        return self.page.content()

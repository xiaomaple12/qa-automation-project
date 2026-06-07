import pytest
from pages.login_page import LoginPage


@pytest.mark.secure
def test_logout(page):
    login_page = LoginPage(page)

    login_page.goto()
    secure_page = login_page.login_and_verify_success()

    secure_page.logout()

    login_page.expect_logout_success()

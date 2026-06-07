import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_text, is_success",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", True),
        ("wrong_user", "SuperSecretPassword!", "Your username is invalid!", False),
        ("tomsmith", "wrong_pass", "Your password is invalid!", False),
        ("", "SuperSecretPassword!", "Your username is invalid!", False),
        ("tomsmith", "", "Your password is invalid!", False),
        ("", "", "Your username is invalid!", False),
    ]
)
def test_login(page, username, password, expected_text, is_success):
    login_page = LoginPage(page)

    login_page.goto()
    login_page.expect_login_page_loaded()
    login_page.login(username, password)

    if is_success:
        secure_page = SecurePage(page)
        secure_page.expect_secure_page_loaded()

        secure_page.logout()
        login_page.expect_logout_success()
    else:
        login_page.expect_error_message(expected_text)

    print(f"測試完成：{username} / {password}")

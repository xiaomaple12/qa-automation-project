import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.mark.parametrize(
    "username, password, expected_text, is_success",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", True),
        ("wrong_user", "SuperSecretPassword!", "Your username is invalid!", False),
        ("tomsmith", "wrong_pass", "Your password is invalid!", False),
    ]
)
def test_login(page, username, password, expected_text, is_success):
    login_page = LoginPage(page)

    login_page.goto()
    login_page.login(username, password)

    page.wait_for_timeout(2000)

    if is_success:
        secure_page = SecurePage(page)

        # 🔥 驗證登入成功
        actual_text = secure_page.get_flash_message()
        assert expected_text in actual_text

        # 🔥 點登出
        secure_page.logout()
        page.wait_for_timeout(2000)

        # 🔥 驗證是否回到登入頁
        page_text = login_page.get_page_text()
        assert "You logged out of the secure area!" in page_text

    else:
        actual_text = login_page.get_page_text()
        assert expected_text in actual_text

    print(f"測試完成：{username} / {password}")

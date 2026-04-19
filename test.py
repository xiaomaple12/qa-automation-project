from playwright.sync_api import sync_playwright

# 🔹 登入功能
def login(page, username, password):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click('button[type="submit"]')

# 🔹 驗證登入成功
def verify_login_success(page):
    page.wait_for_timeout(2000)
    page_text = page.content()
    assert "You logged into a secure area!" in page_text

# 🔹 驗證登入失敗
def verify_login_failed(page):
    page.wait_for_timeout(2000)
    page_text = page.content()
    assert "Your username is invalid!" in page_text

# 🔹 主程式
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # ✅ 測試1：正確登入
    login(page, "tomsmith", "SuperSecretPassword!")
    verify_login_success(page)
    print("測試1成功：正確帳密可以登入")

    # ❌ 測試2：錯誤帳號
    login(page, "wrong_user", "SuperSecretPassword!")
    verify_login_failed(page)
    print("測試2成功：錯誤帳號被擋下")

    page.wait_for_timeout(5000)
    browser.close()

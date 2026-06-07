# QA Automation Test Project

這是一個使用 Python、Pytest 與 Playwright 建立的自動化測試練習專案，主要目的是練習 QA 自動化測試的基本流程，包含測試環境建立、Page Object Model、測試案例撰寫、測試執行與測試報告產出。

本專案測試網站為 The Internet Herokuapp 的 Login Page，用來練習登入流程、錯誤訊息驗證、登入後頁面驗證與登出流程。

## 專案目的

本專案用來練習網頁自動化測試，模擬 QA 在測試登入功能時，如何透過自動化測試確認功能是否符合預期。

目前測試重點包含：

* 登入頁面是否正常載入
* 正確帳號密碼是否能成功登入
* 錯誤帳號是否顯示正確錯誤訊息
* 錯誤密碼是否顯示正確錯誤訊息
* 空帳號或空密碼是否顯示錯誤訊息
* 成功登入後是否進入 secure page
* 登出後是否顯示成功登出訊息

## 使用工具

* Python
* Pytest
* Playwright
* pytest-html
* Git / GitHub

## 專案結構

```text
qa-project/
├── pages/
│   ├── login_page.py
│   └── secure_page.py
├── tests/
│   ├── test_login.py
│   └── test_secure_page.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── report.html
└── README.md
```

## 安裝方式

請先確認電腦已安裝 Python。

建立虛擬環境：

```bash
python -m venv venv
```

啟用虛擬環境：

```bash
.\venv\Scripts\Activate.ps1
```

安裝套件：

```bash
pip install -r requirements.txt
```

安裝 Playwright 瀏覽器：

```bash
playwright install
```

## 執行測試方式

執行全部測試：

```bash
python -m pytest -s
```

只執行 login 標記的測試：

```bash
python -m pytest -m login -s
```

只執行 secure 標記的測試：

```bash
python -m pytest -m secure -s
```

產生 HTML 測試報告：

```bash
python -m pytest --html=report.html
```

## 測試項目

### Login 測試

`tests/test_login.py` 使用 `pytest.mark.parametrize` 進行資料驅動測試，目前包含以下情境：

1. 正確帳號與密碼登入，預期成功進入 secure page
2. 錯誤帳號與正確密碼，預期顯示 username 錯誤訊息
3. 正確帳號與錯誤密碼，預期顯示 password 錯誤訊息
4. 空帳號與正確密碼，預期顯示 username 錯誤訊息
5. 正確帳號與空密碼，預期顯示 password 錯誤訊息
6. 空帳號與空密碼，預期顯示 username 錯誤訊息

### Secure Page 測試

`tests/test_secure_page.py` 測試登入成功後進入 secure page，並執行 logout，最後確認登出成功訊息是否正確顯示。

## 測試報告

專案可透過 pytest-html 產生 `report.html` 測試報告，用來查看測試執行結果。

測試成功時，終端機會顯示類似：

```text
7 passed in xx.xxs
```

代表 pytest 成功找到並執行測試案例，且測試全部通過。

## 學習重點

透過這個專案，我練習了：

* 使用 Playwright 操作瀏覽器進行自動化測試
* 使用 Pytest 撰寫與執行測試案例
* 使用 `pytest.mark.parametrize` 建立多組測試資料
* 使用 fixture 管理測試前置設定
* 使用 Page Object Model 分離頁面操作邏輯與測試案例
* 使用 pytest marker 分類測試，例如 login 與 secure
* 使用 requirements.txt 管理專案套件
* 使用 pytest-html 產生測試報告
* 使用 Git / GitHub 管理專案版本
* 在不同電腦重新建立環境並成功執行測試，確認專案具有基本可重現性

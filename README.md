# QA Automation Project

This project is a QA automation testing project built using Python, Playwright, and pytest.

It demonstrates a complete end-to-end testing flow with a structured and maintainable design.

---

## 🔧 Tech Stack

- Python
- Playwright
- pytest

---

## 📁 Project Structure

qa-project/

├─ pages/

│ ├─ login_page.py

│ └─ secure_page.py

├─ tests/

│ └─ test_login.py

├─ conftest.py

├─ requirements.txt


---

## 🧪 Test Scenario

This project covers a complete login and logout flow:

- Login with valid credentials → Navigate to secure page → Logout → Verify logout success
- Login with invalid username → Show error message
- Login with invalid password → Show error message

---

## 🔁 Key Features

### ✅ Page Object Model (POM)
- Separates page logic from test logic
- Improves maintainability and readability

### ✅ Data-driven Testing
- Uses pytest `parametrize` to test multiple scenarios
- Avoids duplicated test code

### ✅ Multi-page Flow Testing
- Covers full user journey:
  - Login Page → Secure Page → Logout → Back to Login Page

### ✅ Fixture Management
- Uses pytest fixture to handle browser setup and teardown

---

## 🚀 How to Run

```bash
# create virtual environment
python -m venv venv

# activate (Windows)
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# install browser
python -m playwright install

# run tests
python -m pytest -s

---

## 📊 Test Report

The test report can be found here:

- https://xiaomaple12.github.io/qa-automation-project/report.html

---

💡 What I Learned
How to build an automation testing framework using pytest
How to apply Page Object Model (POM) for better code structure
How to design data-driven test cases using parametrize
How to handle multi-page testing flow
Basic Git and GitHub workflow for project management

📌 Notes

This project is created for learning QA automation and preparing for QA-related roles.
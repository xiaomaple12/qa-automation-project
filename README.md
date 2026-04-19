\# QA Automation Project



This is a QA automation testing project built with Python, Playwright, and pytest.



\## 🔧 Tech Stack

\- Python

\- Playwright

\- pytest



\## 📁 Project Structure



qa-project/

├─ pages/

│ ├─ login\_page.py

│ └─ secure\_page.py

├─ tests/

│ └─ test\_login.py

├─ conftest.py

├─ requirements.txt





\## 🧪 Test Scenario



This project covers a complete login flow:



\- Login with valid credentials → success page → logout

\- Login with invalid username → error message

\- Login with invalid password → error message



\## 🔁 Features



\- Page Object Model (POM)

\- Data-driven testing (pytest parametrize)

\- Multi-page flow testing

\- Fixture for browser setup



\## 🚀 How to Run



```bash

\# create virtual environment

python -m venv venv



\# activate

venv\\Scripts\\activate



\# install dependencies

pip install -r requirements.txt



\# install browsers

python -m playwright install



\# run tests

python -m pytest -s



Notes

This project is for learning QA automation and demonstrating testing skills.






# 🚀 Hybrid Data-Driven Test Automation Framework

![Automated Pytest CI with Allure](https://github.com/Akansha051991/pytest-selenium-pom-framework/actions/workflows/pytest_ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.x-orange.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)
![Allure Report](https://img.shields.io/badge/Allure-Reporting-yellow.svg)

A robust, enterprise-grade **Hybrid Test Automation Framework** built with Python, Selenium WebDriver, and Pytest. Designed following the **Page Object Model (POM)** design pattern, supporting multi-browser execution, data-driven testing, parallel test execution, and continuous integration with automated failure reporting.

---

## 🌟 Key Features

* **Page Object Model (POM):** Clean separation of test scripts and page locators/actions for high maintainability and code reusability.
* **Hybrid Data-Driven Architecture:** Supports external data inputs (JSON/CSV/Config) to run tests across multiple data sets dynamically.
* **Multi-Browser & Cross-Environment Support:** Seamlessly executes tests on **Chrome, Firefox, and Microsoft Edge**.
* **Headless CI/CD Execution:** Automatically detects cloud environments (GitHub Actions) to execute browser tests in optimized headless mode (`--headless=new`).
* **Parallel Test Execution:** Powered by `pytest-xdist` (`-n auto`) to drastically reduce suite execution time.
* **Advanced Failure Handling & Allure Reporting:** 
  * Automatically captures screenshots on test failure.
  * Embeds screenshots directly into **Allure Reports** and `pytest-html` reports for fast root-cause analysis.
* **Continuous Integration (CI/CD):** Fully integrated with **GitHub Actions** to run regression suites automatically on every push and pull request.

---

## 📁 Project Architecture

```text
pytest-selenium-pom-framework/
│
├── .github/
│   └── workflows/
│       └── pytest_ci.yml       # GitHub Actions CI/CD pipeline workflow
├── pages/                      # Page Object Model classes (locators & actions)
├── tests/                      # Test scripts (UI & API regression suite)
├── utils/                      # Helper utilities (ConfigReader, Logger, etc.)
├── reports/                    # Local failure screenshots & HTML reports
├── allure-results/             # Raw Allure result data files
├── conftest.py                 # Pytest fixtures, multi-browser setup & failure hooks
├── pytest.ini                  # Pytest configuration and custom markers
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.12
* **Automation Tool:** Selenium WebDriver 4.x
* **Test Framework:** Pytest, pytest-xdist, pytest-html
* **Reporting:** Allure Framework, Pytest-HTML
* **CI/CD:** GitHub Actions (Linux Runners)
* **Design Pattern:** Page Object Model (POM)

## ⚙️ Setup and Installation

1.Clone the repository:
```bash
  git clone https://github.com/Akansha051991/pytest-selenium-pom-framework.git
  cd pytest-selenium-pom-framework
   ```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
 ```
3. Install dependencies:
```bash
pip install -r requirements.txt
 ```
  ## How to Run Tests

* Run all tests locally (headed mode):
  ```bash
   pytest
    ```
* Run tests in Headless mode:
  ```bash
  pytest --headless=true
    ```
* Run tests in parallel across CPU cores:
  ```bash
   pytest -n auto
    ```
* Run tests on a specific browser:
  ```bash
   pytest --browser=firefox
    ```
*  Generate and view Allure Report locally:
   ```bash
   pytest --alluredir=allure-results
    allure serve allure-results
    ```
 ## 📊 CI/CD Pipeline Workflow
   
<p style="font-size: 0.85em; color: #8b949e;">The automated GitHub Actions workflow (<code style="font-size: 0.9em;">pytest_ci.yml</code>) triggers on every push and pull request to the main/feature branches. It performs the following steps:</p>

* Sets up Python 3.12 environment on Ubuntu runner.

* Installs dependencies and Google Chrome / WebDriver.

* Executes the test suite in parallel with headless browser settings.

* Uploads Allure test execution results as downloadable artifacts for auditing.

   ---

### Author Section

```
👨‍💻 Author
Akansha Choudhary
GitHub: [@Akansha051991](https://github.com/Akansha051991)
Feel free to reach out if you have any questions or suggestions regarding QA automation and test architectures!
  ```

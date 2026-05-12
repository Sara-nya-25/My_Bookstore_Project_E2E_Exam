# 📚 My Bookstore Project - E2E Test Automation

This project contains an automated End-to-End (E2E) test suite for the [Bookstore Exam Site](https://tap-ht25-testverktyg.github.io/exam/). It uses **Python**, **Behave (BDD)**, and **Playwright** to verify book catalog management.

## 🚀 Features Tested
* **Add New Books:** Verifies that users can add titles and authors to the catalog.
* **UI Tab Navigation:** Ensures correct behavior when switching between the "Add Book" form and the "Catalog" list.
* **Input Validation:** Checks that the "Add" button is disabled when fields are incomplete.
* **Localization Resilience:** Tests are designed to handle automatic browser translations using Regex patterns.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd My_Bookstore_Project_E2E_Exam

2. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
   
3. **Install dependencies:**
    ```bash
    pip install behave playwright
    playwright install chromium

## 🧪 Running Tests

#### **To run the full test suite:**
    ```bash
    behave

#### **To run a specific feature:**
    ```bash
    behave features/add_book.feature

## 🏗️ CI/CD
This project uses GitHub Actions to automatically run tests on every push to the main or master branch.

### **How to Trigger the CI**
1. **Commit your changes:**
    ```bash
    git add .
    git commit -m "Add README and GitHub Actions CI workflow"
2. **Push to GitHub:**
    ```bash
    git push origin main
3. **Check Results:**
   - Go to your repository on GitHub.
   - Click the "Actions" tab.
   - You will see a workflow named "Playwright Tests" running. If it turns green, your code is officially "CI Verified"!

### 💡 Why this CI setup is smart:
- **--with-deps:** This command ensures that the Linux environment in GitHub has all the necessary system libraries to run a "headless" browser.

- **Automated Feedback:** If you ever make a change that accidentally breaks the "Pippi" regex or the tab switching, GitHub will alert you immediately with a red "X".
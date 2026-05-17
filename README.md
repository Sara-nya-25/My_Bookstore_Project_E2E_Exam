# 📚 My Bookstore Project - E2E Test Automation

This project contains an automated End-to-End (E2E) test suite for the [Bookstore Exam Site](https://tap-ht25-testverktyg.github.io/exam/). 
This project utilizes a Behavior-Driven Development (BDD) approach to validate core user journeys, catalog management, and application reading statistics.
This project uses TDD approach to test the core backend logic using unit and integration tests.

## 🛠️ Tech Stack & Architecture

* **Automation Framework:** [Behave](https://behave.readthedocs.io/)
* **Browser Automation Engine:** [Playwright for Python](https://playwright.dev/python/)
* **Unit/Integration Testing:** [Pytest](https://docs.pytest.org/)
* **Testing Methodology:** Behavior-Driven Development (BDD) / Acceptance Testing

### 📐 The Testing Pyramid Breakdowns

* **70% Unit Tests (Driven by TDD):** Located under `tests/unit/`. These cover every minor edge case of string formatting, mathematical statistics calculations, and server-side data validation rules quickly and in absolute isolation.
* **20% Integration Tests:** Located under `tests/integration/`. These secure critical API endpoint paths and structural database state transitions, confirming that separate modules seamlessly communicate.
* **10% End-to-End & UI Tests (Driven by BDD):** Located under `features/`. These use Playwright and Behave to mimic real human journeys—such as creating accounts, saving titles, interacting with toggle attributes, and validating live math updates on the UI.

> **Why this breakdown?** Over-indexing on high-level E2E tests makes a test suite slow, expensive to run in deployment pipelines, and vulnerable to "flakiness" (failing due to network timing rather than logic bugs). Using unit tests for isolated heavy lifting and E2E for critical paths guarantees a fast, reliable, and bug-free delivery pipeline.

## 📁 Project Structure

The project structure is split between behavior-driven acceptance tests and micro-level unit/integration tests:

```text
My_Bookstore_Project_E2E_Exam/
│
├── .github/                     # CI/CD Workflows
└── Backend/                     # Core application and automation testing root
    ├── features/                # BDD Behavior Specifications
    │   ├── steps/               # Step Definition Implementations
    │   │   └── __init__.py
    │   ├── add_book.feature     # Scenario for adding new titles
    │   ├── catalog.feature      # Scenario for verifying book entry details
    │   ├── environment.py       # Hooks managing Playwright lifecycle (contexts/pages)
    │   ├── favorites.feature    # Scenario for marking titles with heart reactions
    │   ├── navigation.feature   # Scenario for tab swapping behaviors
    │   └── statistics.feature   # Scenario for total book metrics verification
    │
    ├── src/                     # Core production application source code
    │
    ├── tests/                   # Developer TDD Testing Suite
    │   ├── integration/         # Integration tests
    │   └── unit/                # functional unit tests
    │
    ├── Acceptance_criteria.md   # Project acceptance criteria requirements
    ├── Answers.md               # Theoretical question responses
    ├── behave.ini               # Configuration profile for Behave runtime parameters
    ├── pytest.ini               # Configuration profile for Pytest execution limits
    ├── README.md                # Project documentation guide
    └── Stories.md               # User Stories mapping overview
```
## 🚀 Features Tested
* **Add New Books:** Verifies that users can add titles and authors to the catalog.
* **UI Tab Navigation:** Ensures correct behavior when switching between the "Add Book" form and the "Catalog" list.
* **Input Validation:** Checks that the "Add new book" button is disabled when fields are incomplete.
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
   pip install -r requirements.txt

4. **Install Playwright browser binaries:**   
   ```bash   
    playwright install chromium
   
## 🧪 Running Tests

#### To run the full test suite:

   ```bash   
      behave
   ```
#### To display print() logs or live debugging outputs without background capture, run:

   ```bash
      behave --no-capture 
   ```
#### To run a specific feature:

   ```bash
      behave features/add_book.feature
   ``` 
   
### 🏗️ CI/CD
This project uses GitHub Actions to automatically run tests on every push to the main or master branch.
All implemented unit, integration, and behavioral specs are automated to execute seamlessly as continuous **Regression Tests** within the project's CI/CD environment pipelines (`.github/`), 
guaranteeing that code additions or hotfixes never degrade pre-existing functionality.


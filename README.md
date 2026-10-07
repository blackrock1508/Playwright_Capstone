# Playwright Python Automation Capstone Project

## 1. Project Overview

This repository contains a complete Playwright Python automation framework for UI and API testing. It demonstrates a full automation lifecycle, including Page Object Model (POM), data-driven testing, parallel execution, logging, diagnostics, reporting, CI/CD, artifact collection, and email notifications.

## 2. Business Requirements

The framework supports:

- Smoke and regression testing
- UI automation
- API automation
- Data-driven testing
- Parallel execution
- Failure diagnostics
- CI execution
- Reporting and notifications

## 3. Framework Structure

```text
playwright-capstone/
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── registration_page.py
├── tests/
│   ├── ui/
│   └── api/
├── testdata/
│   ├── login_data.json
│   └── registration_data.json
├── utils/
│   ├── logger.py
│   ├── json_utils.py
│   └── session_storage.py
├── logs/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── report.html
├── .gitignore
└── README.md
```

## 4. UI Automation

The framework covers:

- Valid login
- Invalid login
- Product display validation
- Add/remove cart items
- Product details
- Sorting
- Checkout flow

It uses semantic locators such as `get_by_role()`, `get_by_text()`, and `get_by_label()`.

## 5. Page Object Model

All locators and actions are encapsulated in dedicated page object classes to reduce duplication and improve maintainability.

## 6. Data-Driven Testing

The framework uses JSON-based test data with `@pytest.mark.parametrize` to validate multiple scenarios efficiently.

## 7. Fixtures, Hooks, and Markers

Supported markers:

- `smoke`
- `regression`
- `readonly`

Fixtures include browser and page setup with teardown handling.

## 8. Multiple Windows / Tabs

The framework uses `page.context.expect_page()` to validate parent-child window interactions.

## 9. Wait Handling

The suite includes both implicit and explicit waits such as:

- `locator.wait_for()`
- `page.wait_for_url()`
- `page.wait_for_load_state()`

## 10. API Automation

The project includes more than five API tests covering:

- GET
- POST
- PUT/PATCH
- DELETE

## 11. API Response Model

A response model class encapsulates JSON fields for structured validation.

## 12. Search Without Index

The framework supports searching JSON objects by business keys without relying on index-based access.

## 13. Deep JSON Comparison

A reusable deep comparison utility validates nested JSON structures accurately.

## 14. Session Storage

Functions exist to save, read, clear, and restore `sessionStorage` values during test execution.

## 15. Logging

Python logging is configured for test execution and writes to the project log files.

## 16. Failure Artifacts

Playwright artifacts include:

- Traces
- Screenshots
- Videos

## 17. HTML Reporting

Generate an HTML report with:

```bash
pytest --html=report.html --self-contained-html
```

## 18. Git and GitHub Workflow

The project includes standard Git workflows such as branching, pull request creation, and merge practices.

## 19. .gitignore

The repository excludes generated and environment-specific files such as logs, screenshots, caches, and virtual environments.

## 20. GitHub Actions CI

The CI workflow includes:

- Checkout
- Python setup
- Dependency installation
- Playwright installation
- Test execution
- HTML report generation
- Artifact upload
- Email notification

## 21. Workflow Triggers

Supported triggers:

- `push`
- `pull_request`
- `workflow_dispatch`

## 22. Artifact Upload

The workflow uploads both the HTML report and failure artifacts for troubleshooting and reporting.

## 23. Email Notification

Email notifications can include:

- Execution status
- Workflow metadata
- Artifact URL
- HTML report attachment

## 24. Summary

This project is designed as a complete end-to-end automation framework for validating both UI and API behavior with a structured, maintainable, and CI-friendly testing approach.

from pages.login_pages import swaglab_Login
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def shared_page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    print(f"Test {item.name} - {report.outcome}")
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is None:
            page = item.funcargs.get("shared_page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
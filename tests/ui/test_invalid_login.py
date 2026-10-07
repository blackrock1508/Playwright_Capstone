import json

from playwright.sync_api import expect
import pytest
from pathlib import Path
from pages.login_pages import swaglab_Login

# Load invalid login data from JSON file
with open(Path("testdata/invalid_login_data.json")) as f:
    invalid_login_data = json.load(f)
import logging


logfolder = Path("logs")
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "invalid_login_test.log"
logger= logging.getLogger("InvalidLoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='w')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)   

@pytest.mark.smoke
@pytest.mark.parametrize("invalid_login_data", invalid_login_data)

def test_login_page(invalid_login_data,shared_page):
    logger.info("Starting invalid login test.")
    try:
        logger.info("Starting invalid login test.")
        login_page = swaglab_Login(shared_page)
        login_page.navigate_to_login_page()
        logger.info("Navigated to login page.")
        login_page.fill_username(invalid_login_data["username"])
        logger.info(f"Filled username: {invalid_login_data['username']}")
        login_page.fill_password(invalid_login_data["password"])
        logger.info('Password filled.')
        login_page.click_login()    
        logger.info(f"Attempting to log in with username: {invalid_login_data['username']}")
        login_page.error_message.wait_for(state="visible")  # Wait for the error message to appear
        assert login_page.error_message.is_visible(), "Error message is not visible, login might have succeeded unexpectedly."
        logger.info("Error message is visible.")
        #expect(login_page.locator("#userName-value")).to_have_text(invalid_login_data["username"])
        expected_error_message = invalid_login_data["error_message"]
        expect(login_page.error_message).to_have_text(expected_error_message)
        logger.info(f"Login failed for user: {invalid_login_data['username']}")
    except AssertionError as e:
        logger.error(f"Invalid login test failed for user: {invalid_login_data['username']}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise
    logger.info("Invalid login test completed.")
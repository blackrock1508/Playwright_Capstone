import json

from playwright.sync_api import expect
import pytest
from pathlib import Path
from pages.login_pages import swaglab_Login
from pages.login_pages import invetory_page

# Load login data from JSON file
with open(Path("testdata/login_data.json")) as f:
    login_data = json.load(f)
import logging


logfolder = Path("logs")
logfolder.mkdir(exist_ok=True)
logfile = logfolder / "login_test.log"
logger= logging.getLogger("LoginTestLogger")
logger.setLevel(logging.INFO)
logger.propagate = False
handler = logging.FileHandler(logfile, mode='a')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)   

@pytest.mark.smoke
@pytest.mark.parametrize("login_data", login_data)
def test_login_page(login_data,shared_page):
    try:
        logger.info("Starting login test.")
        login_page = swaglab_Login(shared_page)
        login_page.navigate_to_login_page()
        logger.info("Navigated to login page.")
        login_page.fill_username(login_data["username"])
        logger.info(f"Filled username: {login_data['username']}")
        login_page.fill_password(login_data["password"])
        logger.info('Password filled.')
        login_page.click_login()    
        logger.info(f"Attempting to log in with username: {login_data['username']}")
        inventory_Page = invetory_page(shared_page)
        inventory_Page.click_open_menu()
        logger.info("Clicked on open menu.")
        inventory_Page.logout_link.wait_for(state="visible")  # Wait for the page to load after login
        assert inventory_Page.is_logout_link_visible(), "Logout link is not visible, login might have failed."
        logger.info("Logout link is visible, login was successful.")
        #expect(login_page.locator("#userName-value")).to_have_text(login_data["username"])
        logger.info(f"Login successful for user: {login_data['username']}")
        inventory_Page.click_close_menu()
        logger.info("Closed the menu.")
    except AssertionError as e:
        logger.error(f"Login test failed for user: {login_data['username']}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise
    logger.info("Login test completed.")

pytest.mark.smoke    
def test_validate_products(shared_page):
    try:
        logger.info("Starting product validation test.")
        inventory_Page = invetory_page(shared_page)
        assert inventory_Page.is_inventory_item_visible(), "Inventory items are not visible, product validation might have failed."
        logger.info("Inventory items are visible, product validation was successful.")
        inventory_items = inventory_Page.get_inventory_items()
        logger.info(f"Retrieved inventory items: {inventory_items}")
        inventory_Page.click_close_menu()
        logger.info("Closed the menu.")
    except AssertionError as e:
        logger.error("Product validation test failed.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred during product validation: {e}")
        raise
    logger.info("Product validation test completed.")   

@pytest.mark.smoke    
def test_add_to_cart_and_validate_count(shared_page):
    try:
        logger.info("Starting add to cart test.")
        inventory_Page = invetory_page(shared_page)
        assert inventory_Page.is_inventory_item_visible(), "Inventory items are not visible, cannot add to cart."
        logger.info("Inventory items are visible, proceeding to add to cart.")
        
        inventory_Page.click_on_inventory_item("Sauce Labs Backpack") 
        logger.info("Clicked on the inventory item: Sauce Labs Backpack.")
        inventory_Page.click_add_to_cart()
        logger.info("Clicked on add to cart button.")
        cart_count = inventory_Page.get_cart_count()  # Assuming this method returns the current cart count
        logger.info(f"Retrieved cart count: {cart_count}")
        expected_count = 1  # Replace with the expected count after adding the item
        assert cart_count == expected_count, f"Cart count is {cart_count}, expected {expected_count}."

         # Replace with the actual item name you want to add
        # Assuming there's a method to add an item to the cart, you would call it here
        # For example: inventory_Page.add_item_to_cart(item_name)
        # Then validate the cart count
        # For example: assert inventory_Page.get_cart_count() == expected_count
        logger.info("Item added to cart and count validated successfully.")
    except AssertionError as e:
        logger.error("Add to cart test failed.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred during add to cart test: {e}")
        raise
    logger.info("Add to cart test completed.")

@pytest.mark.smoke
def test_logout(shared_page):
    try:
        logger.info("Starting logout test.")
        inventory_Page = invetory_page(shared_page)
        login_page = swaglab_Login(shared_page)
        inventory_Page.click_open_menu()
        logger.info("Clicked on open menu.")
        inventory_Page.logout_link.wait_for(state="visible")  # Wait for the logout link to be visible
        inventory_Page.click_logout()
        logger.info("Clicked on logout link.")
        login_page.username_input.wait_for(state="visible")  # Wait for the username input to be visible after logout
        assert login_page.username_input.is_visible(), "Username input is not visible, logout might have failed."
        logger.info("Logout was successful, username input is visible.")
    except AssertionError as e:
        logger.error("Logout test failed.")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred during logout: {e}")
        raise
    logger.info("Logout test completed.")
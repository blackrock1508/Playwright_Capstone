

class swaglab_Login:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")
        self.Open_menu = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.error_message = page.locator("h3[data-test='error']")  # Adjust the selector based on the actual error message element
    def navigate_to_login_page(self):
        self.page.goto("https://www.saucedemo.com/")  # Replace with the actual login page URL
            
    def fill_username(self, username):
        self.username_input.fill(username)

    def fill_password(self, password):
        self.password_input.fill(password)  
    def click_open_menu(self):
        self.Open_menu.click()
    def click_login(self):
        self.login_button.click()
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")  # Wait for network to be idle, indicating page load completion

    def is_logout_link_visible(self):
        return self.logout_link.is_visible()
    
    def click_logout(self):
        self.logout_link.click()

    def get_error_message(self):
        return self.error_message.inner_text()   
                   
class invetory_page:
    def __init__(self, page):
        self.page = page
        self.inventory_item =  page.locator("[data-test=\"item-4-title-link\"]")
        #self.inventory_item =page.locator("[data-test=\"back-to-products\"]")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.Open_menu = page.get_by_role("button", name="Open Menu")
        self.close_menu = page.get_by_role("button", name="Close Menu")  # Adjust the selector  
        
    def add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()  # Adjust the selector based on the actual "Add to Cart" button element    
    def remove_from_cart(self):
        self.page.get_by_role("button", name="Remove").click()  # Adjust the selector based on the actual "Remove" button element
    def get_cart_count(self):
        cart_count_element = self.page.locator(".shopping_cart_badge")  # Adjust the selector based on the actual cart count element
        if cart_count_element.is_visible():
            return int(cart_count_element.inner_text())
        return 0
    def click_add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()  # Adjust the selector based on the actual "Add to Cart" button element
    def click_on_inventory_item(self, item_name):
        self.inventory_item.click()  # Adjust the selector based on the actual inventory item element
    def click_open_menu(self):
        self.Open_menu.click()  
    def click_close_menu(self):
        self.close_menu.click()
    def is_logout_link_visible(self):
        return self.logout_link.is_visible()    
    def click_logout(self):
        self.logout_link.click()
    def is_inventory_item_visible(self):
        return self.inventory_item.is_visible()     
    def get_inventory_items(self):
        return self.inventory_item.all_inner_texts()  # Returns a list of all inventory item texts       
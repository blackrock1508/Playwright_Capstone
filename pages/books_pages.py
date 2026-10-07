class books:
    def __init__(self, page):
        self.page = page
        self.books_button = page.get_by_role("button", name="Book Store")
        self.search_box = page.get_by_placeholder("Type to search")
        self.book_title_link = page.locator(".rt-tbody .rt-tr-group .rt-td a")  # Adjust the selector based on the actual book title link element
        self.add_to_collection_button = page.get_by_role("button", name="Add To Your Collection")
        self.profile_button = page.get_by_role("button", name="Profile")
        self.logout_button = page.get_by_role("button", name="Logout") 
        self.delete_account_button = page.get_by_role("button", name="Delete Account")

        
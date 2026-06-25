from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):

        self.page = page

        self.view_cookie = page.get_by_role(
            "button",
            name="View cookies"
        )

        self.close_cookie = page.locator(
            ".save-preference-btn-handler.onetrust-close-btn-handler"
        )

        self.expand_menu = page.get_by_label("Expand menu")
        self.collapse_menu = page.get_by_label("Collapse")

        self.demand_pursuits = page.get_by_label(
            "Demand Pursuits"
        )

        self.create_pursuit = page.get_by_label(
            "Create Pursuit"
        )

    def close_cookie_popup(self):

        self.view_cookie.click()

        self.close_cookie.wait_for(
            state="visible"
        )

        self.close_cookie.click(force=True)

    def validate_dashboard(self):

        expect(
            self.page.get_by_text(
                "Demand Pursuits"
            )
        ).to_be_visible()

    def validate_categories(self):

        categories = [
            "All",
            "New",
            "In Progress",
            "Cancelled",
            "Won",
            "Deferred"
        ]

        for category in categories:

            expect(
                self.page.locator("span")
                .filter(has_text=category)
                .first
            ).to_be_visible()

            print(f"{category} displayed")

    def expand_left_menu(self):

        self.expand_menu.click()

    def validate_left_menu(self):

        expect(self.collapse_menu).to_be_visible()
        expect(self.demand_pursuits).to_be_visible()
        expect(self.create_pursuit).to_be_visible()

    def collapse_left_menu(self):

        self.collapse_menu.click()
    def click_create_pursuit(self):

        self.create_pursuit.click()

       
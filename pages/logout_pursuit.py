from playwright.sync_api import expect

class LogoutPage:
    def __init__(self, page):
        self.page=page

        self.profile_btn = page.locator("span.user-profile-trigger-name")
        self.logout_btn = page.get_by_text("Logout",exact=True)
        self.login_heading =page.get_by_role("heading",name="Login to continue")

    def click_profile(self):
        self.profile_btn.click()
        print("Clicked on profile button")
    
    def click_logout(self):
        self.logout_btn.click()
        print("Clicked on Logout button")
        expect(self.login_heading).to_be_visible()
        print("User Logged out successfully")
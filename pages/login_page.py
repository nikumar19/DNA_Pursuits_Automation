from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.sso_btn = page.get_by_role("button", name="Login using SSO")
        self.username = page.get_by_role("textbox", name="username")
        self.password = page.get_by_role("textbox", name="password")
        self.signin = page.locator("input[name='signInSubmitButton']:visible").first

    def navigate(self):
        print("Navigating to the login page")
        self.page.goto("https://dna-preprod.hashedin.com/pursuits/")

    def login(self, username, password):
        print("Clicking on the SSO button and entering credentials")
        self.sso_btn.click()
        print(f"Entering username: {username} and password: {password}")
        self.username.fill(username)
        self.password.fill(password)
        print("Clicking on the Sign In button")
        self.signin.click()
        
        self.page.wait_for_url(
            "https://dna-preprod.hashedin.com/pursuits",
            timeout=10000
        )
        print("Login Page: Login successful, navigated to the dashboard page")


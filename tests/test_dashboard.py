from textwrap import fill
from playwright.sync_api import expect

from playwright.sync_api import sync_playwright

def test_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        #Login to the application
        page.goto("https://dna-preprod.hashedin.com/pursuits/")
        page.get_by_role("button", name="Login using SSO").click()
        page.get_by_role("textbox", name="username").fill("hashedintestuser108")
        page.get_by_role("textbox", name="password").fill("Hashedintestuser108@12345")
        page.locator("input[name='signInSubmitButton']:visible").first.click()
        page.wait_for_url("https://dna-preprod.hashedin.com/pursuits",timeout=5000)
        page.get_by_role("button", name="View cookies").click()

        #escape the cookie pop upg
        #page.keyboard.press("Escape")

        #select view cookies button and click on it to close the cookie pop up
        page.locator(".save-preference-btn-handler.onetrust-close-btn-handler").wait_for(state="visible")
        page.locator(".save-preference-btn-handler.onetrust-close-btn-handler").click(force=True)

        #validate headiing of the page after login
        expect(page.get_by_text("Demand Pursuits")).to_be_visible()
        print("Login successful")

        # Dashboard Heading Validation
        categories = ["All", "New", "In Progress", "Cancelled", "Won", "Deferred"]

        #printing the categories displayed on the dashboard
        for category in categories:
            expect(page.locator("span").filter(has_text=category).first).to_be_visible()
            print(f"✓ {category} is displayed")

        print("✓ All 6 categories are displayed")

        #  List of all Pursuits
        expect(page.get_by_text("List of all Pursuits")).to_be_visible()
        print("✓ List of all Pursuits is displayed")

        page.get_by_label("Expand menu").click()
        print("✓ Expand menu is displayed")

        #validate the collapse button is displayed after clicking on expand menu
        expect(page.get_by_label("Collapse")).to_be_visible()
        print("✓ Collapse is displayed")

        #
        expect(page.get_by_label("Demand Pursuits")).to_be_visible()
        print("✓ Demand Pursuits is displayed")

        expect(page.get_by_label("Create Pursuit")).to_be_visible()
        print("✓ Create Pursuit is displayed")

        #cliqk on the collapse button to collapse the menu
        page.get_by_label("Collapse").click()
        print("left menu is collapsed")


        
 

        page.wait_for_timeout(10000)
        assert page is not None

        context.close()
        browser.close()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_pursuit_page import CreatePursuitPage
from pages.demand_pursuit import DemandPage
from pages.logout_pursuit import LogoutPage
from faker import Faker
fake = Faker()
client_name = fake.company()

pursuit_data = {

"client_name": client_name,
"pursuit_name": "Automation Test",
"jupiter_id": str(fake.random_number(digits=6)),
"proposal_type": "RFP",
"project_type": "Test Automation",
"country": "India",
"billing_arrangement": "Fixed Fee",
"status": "New"
}


def test_launch():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )
        page = browser.new_page()

        login = LoginPage(page)
        dashboard = DashboardPage(page)
        create_pursuit = CreatePursuitPage(page)
        demand_pursuit = DemandPage(page)
        logout = LogoutPage(page)

        login.navigate()

        login.login(
            "hashedintestuser108",
            "Hashedintestuser108@12345"
        )
        dashboard.close_cookie_popup() 
        dashboard.validate_dashboard()
        dashboard.validate_categories()
        dashboard.expand_left_menu()
        print("Clicking on the Create Pursuit button")
        dashboard.click_create_pursuit()
        print("Validating the Create Pursuit page")
        create_pursuit.validate_buttons()
        print("Clicking on the Create button without filling any details")
        create_pursuit.click_create()
        print("Validating the required errors displayed for all mandatory fields")
        create_pursuit.validate_required_errors()
        create_pursuit.add_new_client(client_name)
        print("Selecting the Industry from the dropdown")
        create_pursuit.select_industry()
        print("Industry selected successfully")
        create_pursuit.select_sector()
        print("Selecting the Sector from the dropdown")
        print("Sector selected successfully")
        print("Clicking on the Save button to save the pursuit details")
        create_pursuit.click_save()
        expect(page.get_by_label("Create Pursuit")).to_be_visible()
        print("✓ Create Pursuits is displayed")
        print("Selecting the Proposal Type from the dropdown")
        create_pursuit.select_proposal_type()
        create_pursuit.select_project_type()
        create_pursuit.create_pursuit(pursuit_data)
        create_pursuit.select_country()
        create_pursuit.select_billing_arrangement()
        create_pursuit.select_project_duration()
        create_pursuit.select_click_create()
        demand_pursuit.search_client(client_name)
        demand_pursuit.validate_pursuit_details(pursuit_data)  
        demand_pursuit.validate_pursuit_details_page()
        logout.click_profile()
        logout.click_logout()
        page.wait_for_timeout(10000)
        browser.close()

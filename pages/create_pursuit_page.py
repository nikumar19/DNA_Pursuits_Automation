from playwright.sync_api import expect
from random import randint
from faker import Faker

class CreatePursuitPage:

    def __init__(self, page):

        self.page = page

        self.create_btn = page.get_by_role(
            "button",
            name="Create",
            exact=True
        )

        self.cancel_btn = page.get_by_role(
            "button",
            name="Cancel",
            exact=True
        )
        self.add_new_client_btn = page.get_by_role(
            "button",
             name="Add New Client",
              exact=True
        )

        self.client_name_popup = page.get_by_placeholder("Add New Client")
        self.save_client_btn = page.get_by_role("button", name="Save", exact=True)

        self.industry_dropdown = page.locator(
             ".ant-modal-content .ant-select"
            ).nth(0)

        self.industry_option = page.get_by_text(
            "Technology Media and Telecom",
            exact=False
        )
        self.sector_dropdown = page.locator(
         ".ant-modal-content .ant-select"
            ).nth(1)

        self.sector_option = page.locator(
            ".ant-select-item-option-content"
        ).filter(has_text="Telecommunications").first
        
        self.save_btn = page.get_by_role(
            "button",
            name="Save", 
            exact=True)

        self.create_btn = page.get_by_role(
            "button",
            name="Create",
            exact=True)
            


    def select_proposal_type(self):
        print("Selecting Proposal Type")

        self.page.locator("div .ant-select-selector").nth(1).click()
        self.page.keyboard.type("RFP")
        print("Clicked on Proposal Type dropdown")
        self.page.wait_for_timeout(500)
        
        self.page.keyboard.press("Enter")

        print("Proposal Type selected successfully")

    def select_project_type(self):
        print("Selecting Project Type")

        self.page.locator("div .ant-select-selector").nth(2).click()
        self.page.keyboard.type("Test Automation")
        print("Clicked on Project Type dropdown")
        self.page.wait_for_timeout(500)
        
        self.page.keyboard.press("Enter")

        print("Project Type selected successfully")

    def select_country(self):
        print("Selecting Country")

        self.page.locator("div .ant-select-selector").nth(3).click()
        self.page.keyboard.type("India")
        print("Clicked on Country dropdown")
        self.page.wait_for_timeout(500)
        
        self.page.keyboard.press("Enter")

        print("Country selected successfully")
    
    def select_billing_arrangement(self):
        print("Selecting Billing Arrangement")

        self.page.locator("div .ant-select-selector").nth(4).click()
        self.page.keyboard.type("Fixed Fee")
        print("Clicked on Billing Arrangement dropdown")
        self.page.wait_for_timeout(500)
        
        self.page.keyboard.press("Enter")

        print("Billing Arrangement selected successfully")

    def select_project_duration(self):
        self.page.locator(".ant-picker-range").click()
        # collect enabled date cells and select a start and end date
        dates = self.page.locator(".ant-picker-cell:not(.ant-picker-cell-disabled)")
        dates.nth(0).click()
        dates.nth(5).click()
        self.page.get_by_role("button", name="Done").click()
      

        print("Project Duration selected successfully")
    
    def select_click_create(self):
        self.create_btn.click()
        print("Clicked on the Create button")
        expect(
            self.page.get_by_text("New pursuit is created"
            )).to_be_visible(timeout=5000)
        print("New pursuit is created")

    def select_industry(self):

        print("Before dropdown click")
        self.page.locator(".ant-modal-content .ant-select").first.click(force=True)

        print("After dropdown click")
        self.page.wait_for_timeout(1000)

        self.industry_option.click()
        print("Industry selected")

    def select_sector(self):
        print("Before sector click")
        self.sector_dropdown.click(force=True)
        print("After sector click")
        self.page.wait_for_timeout(1000)
        self.sector_option.click()
        print("Sector selected")

    def click_save(self):
        self.save_btn.click()
        print("Clicked on the Save button")
    
    def create_pursuit(self, data):

        self.page.get_by_placeholder(
        "Enter pursuit name"
        ).fill(data["pursuit_name"])

        self.page.get_by_placeholder(
        "Enter jupiter ID"
        ).fill(data["jupiter_id"])



    def validate_buttons(self):

        expect(self.create_btn).to_be_visible()
        expect(self.cancel_btn).to_be_visible()

        print("Create button displayed")
        print("Cancel button displayed")

    def click_create(self):

        self.create_btn.click()
    
   

    def validate_required_errors(self):

        errors = [

            "Client name is required",
            "Pursuit name is required",
            "Proposal type is required",
            "Project type is required",
            "Country is required",
            "Industry is required",
            "Sector is required",
            "Billing arrangement is required",
            "Date range is required"

        ]
        print("Validating required errors displayed for all mandatory fields")

        for error in errors:

            expect(
                self.page.get_by_text(error)
            ).to_be_visible()

            print(f"{error} displayed")

    def add_new_client(self, client_name):

        self.add_new_client_btn.click()
        self.client_name_popup.fill(client_name)
        self.save_client_btn.click()

        self.page.wait_for_timeout(2000)

        print(f"client '{client_name}' added successfully")
from playwright.sync_api import expect

class DemandPage:
    def __init__(self, page):
        self.page=page
        self.search_icon = self.page.locator(
        "button.pursuit-search-button")

        self.search_box= self.page.locator(
        "input[placeholder='Search Client, Pursuit, JupiterID']"
        )
        self.pursuit_details = page.get_by_role("heading", name="Pursuit Details")

    def search_client(self, client_name):
        self.page.wait_for_load_state("networkidle")
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.search_icon.click()
        self.page.wait_for_timeout(1000)
        self.search_box.fill(client_name)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(10000)
        print(f"Searching for client : {client_name}")

    def validate_pursuit_details(self,pursuit_data):
        row = self.page.locator("tbody tr:not(.ant-table-measure-row)")

        for i in range(row.count()):
            print(i, row.nth(i).text_content())
        
        expect(row).to_contain_text(pursuit_data["client_name"][:12])
        print("Client name vaildated")
        expect(row).to_contain_text(pursuit_data["pursuit_name"])
        print("Pursuit Name Vaildated")
        expect(row).to_contain_text(pursuit_data["proposal_type"])
        print("Proposal Type Validated")
        expect(row).to_contain_text(pursuit_data["country"])
        print("Country Validated")
        # expect(row).to_contain_text(pursuit_data["billing_arrangement"])
        expect(row).to_contain_text(pursuit_data["jupiter_id"])
        print("Jupiterb Id Validated")
        print("All pursuit detaild validated")

      

    def validate_pursuit_details_page(self):
        row = self.page.locator("tbody tr:not(.ant-table-measure-row)")
        row.click()
        print("Clicked on newly created pursuit")
        expect(self.pursuit_details).to_be_visible()
        print("Pursuit Details is deplayed Successfully")
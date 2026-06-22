from playwright.sync_api import sync_playwright

def test_launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://dna-preprod.hashedin.com/pursuits/")
        page.get_by_role("button", name="Login using SSO").click()
        page.wait_for_timeout(10000)
        assert page is not None

        context.close()
        browser.close()
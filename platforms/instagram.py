from playwright.sync_api import sync_playwright

def get_ig_acc(username):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page(locale="en-US")
        page.goto(f"https://www.instagram.com/{username}/")
        page.wait_for_timeout(4000)
        text = page.inner_text("body")
        browser.close()

        if "accounts/login" in page.url:
            result = "[-] Request could not proceed!"
        elif "isn't available" in text:
            result = "[-] Instagram was not found!"
        else:
            result = f"[+] Instagram was found! -> https://instagram.com/{username}"

        return result
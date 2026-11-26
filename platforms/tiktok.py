from playwright.sync_api import sync_playwright

def get_tt_acc(username):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page(locale="en-US")
        page.goto(f"https://www.tiktok.com/@{username}/")
        page.wait_for_timeout(4000)
        text = page.inner_text("body")
        browser.close()

        if "accounts/login" in page.url:
            result = "[-] Request could not proceed!"
        elif "Couldn't find this account" in text:
            result = "[-] TikTok was not found!"
        else:
            result = f"[+] TikTok was found! -> https://tiktok.com/{username}"

        return result
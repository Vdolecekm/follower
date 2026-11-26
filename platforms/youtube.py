from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

def get_yt_acc(username):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page(locale="en-US")
        x = page.goto(f"https://www.youtube.com/@{username}")

        if "consent.youtube.com" in page.url:
            page.get_by_role("button", name="Reject all").click()
            page.wait_for_url("https://www.youtube.com/**", timeout=15000)

        page.wait_for_timeout(4000)
        text = page.inner_text("body")
        browser.close()

    if "Before you continue" in text:
        result = "[-] Request could not proceed!"
    if x.status == 404 or not text:
        result = "[-] Youtube was not found!"
    else:
        result = f"[+] Youtube was found! -> https://youtube.com/{username}"
    
    return result
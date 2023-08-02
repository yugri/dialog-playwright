import logging
from playwright.sync_api import sync_playwright

MEETING_URL = "https://us05web.zoom.us/j/2885613841?pwd=VnZTMDR2WGVmMi96c251bGNTQTdyZz09"


def connect_to_zoom_meeting_directly(
    meeting_url: str,
) -> None:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(
            headless=False,
            firefox_user_prefs={
                "permissions.default.microphone": 1,
                "permissions.default.camera": 1,
            },
        )
        context = browser.new_context(locale="en-us")
        page = context.new_page()
        page.goto(meeting_url)
        page.on("dialog", lambda dialog: dialog.accept())
        page.goto(f"{MEETING_URL}#success")
        page.get_by_role("button", name="Launch Meeting").click()
        page.get_by_role("button", name="Join from Your Browser").click()
        page.get_by_label("Your Name").click()
        page.get_by_label("Your Name").fill("Johny Mnem")
        page.get_by_role("button", name="Join Audio").click()
        page.get_by_role("button", name="Join").click()
        browser.close()


if __name__ == "__main__":

    logging.info(f"Connecting to meeting: {MEETING_URL}")

    connect_to_zoom_meeting_directly(MEETING_URL)

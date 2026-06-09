"""eyes for the web. playwright drives a real browser; fable reads screenshots.

first capability: window-shopping amazon. it scrolls, it looks, it has
opinions. buying is a later problem.
"""

from playwright.sync_api import sync_playwright


def window_shop(query: str, screenshot_path: str = "journal/seen.png") -> str:
    """search amazon, scroll a bit, screenshot what fable saw."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.amazon.co.uk/s?k={query}", timeout=60000)
        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(1500)
        page.screenshot(path=screenshot_path, full_page=False)
        browser.close()
    return screenshot_path

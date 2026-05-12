import sys
import os
from playwright.sync_api import sync_playwright
# This adds the 'Backend' directory to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def before_all(context):
    # Start Playwright
    context.playwright = sync_playwright().start()
    # Launch browser (headless=False lets you see the browser during local runs)
    context.browser_instance = context.playwright.chromium.launch(headless=False, slow_mo=1000)
    # Create a new browser context (similar to a clean incognito window)
    context.browser_context = context.browser_instance.new_context(locale="en-US", extra_http_headers={"Accept-Language": "en-US,en;q=0.9"})
    # Create the page object
    context.page = context.browser_context.new_page()

def after_all(context):
    # Clean up
    context.browser_instance.close()
    context.playwright.stop()
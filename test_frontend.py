from playwright.sync_api import sync_playwright
import time

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # 1. Test Theme Toggle
        theme_btn = page.locator("#nav-theme")
        theme_btn.click()
        assert "dark" in page.evaluate("document.documentElement.className")
        print("Theme toggle to dark mode works!")

        # 2. Test About Modal
        about_btn = page.locator("#nav-about")
        about_btn.click()
        page.wait_for_selector("#doc-modal:not(.hidden)")
        # Wait for "Loading Document..." to change to "About Project"
        page.wait_for_function('document.getElementById("doc-modal-title").textContent === "About Project"')
        print("About modal loads README.md correctly!")

        # Close About Modal
        close_doc_btn = page.locator("#close-doc-modal")
        close_doc_btn.click()
        time.sleep(0.5) # Wait for animation

        # 3. Test Print Modal
        print_btn = page.locator("#nav-print")
        print_btn.click()
        page.wait_for_selector("#print-modal:not(.hidden)")
        time.sleep(0.5) # Wait for animation

        checkboxes = page.locator("#print-checkboxes input[type='checkbox']")
        count = checkboxes.count()
        assert count > 0
        print(f"Print modal populated with {count} document checkboxes!")

        # Uncheck all but the first one to keep the test quick
        for i in range(1, count):
            checkboxes.nth(i).uncheck()

        # We can't easily intercept `window.print` in a basic playwright script without more setup,
        # but we can submit the form and ensure the `#print-area` gets populated.

        page.evaluate("window.print = function() { window._printCalled = true; }")
        submit_btn = page.locator("#submit-print-btn")
        submit_btn.click()

        # Wait for rendering to complete (window.print gets called)
        page.wait_for_function('window._printCalled === true', timeout=10000)

        # Verify print area has content
        print_area = page.locator("#print-area")
        assert print_area.inner_html().strip() != ""
        print("Print area populated and window.print() triggered successfully!")

        browser.close()

if __name__ == "__main__":
    test()

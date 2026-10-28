"""
DevOps Practical 11: Selenium Web Automation Test
Searches for 'DevOps' on Google and verifies/prints page title.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_devops_search_test():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Uncomment for headless execution in CI/CD environments

    print("[*] Initializing ChromeDriver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("[*] Opening https://www.google.com ...")
        driver.get("https://www.google.com")
        driver.maximize_window()
        time.sleep(2)

        print("[*] Locating search input box and entering 'DevOps'...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys("DevOps")
        search_box.send_keys(Keys.RETURN)

        print("[*] Waiting for search results to load...")
        time.sleep(3)

        page_title = driver.title
        print("\n" + "=" * 45)
        print("RESULT - Page Title is:", page_title)
        print("=" * 45 + "\n")

        assert "DevOps" in page_title, "Verification Failed: 'DevOps' not in page title"
        print("[SUCCESS] Test Passed: Successfully queried DevOps on Google.")

    finally:
        print("[*] Closing browser session...")
        driver.quit()

if __name__ == "__main__":
    run_devops_search_test()


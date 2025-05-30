from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ─── SETUP ─────────────────────────────────────────────────────────
options = Options()
options.add_experimental_option("detach", True)  # keep browser open

service = Service(ChromeDriverManager().install())
driver  = webdriver.Chrome(service=service, options=options)

# ─── DEMO ──────────────────────────────────────────────────────────
driver.get("https://google.com")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("programming market in 2025", Keys.RETURN)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "search"))
)
driver.find_element(By.CSS_SELECTOR, "h3").click()

# ─── PAUSE & CLEANUP ───────────────────────────────────────────────
input("Demo complete—press Enter to close browser")
driver.quit()

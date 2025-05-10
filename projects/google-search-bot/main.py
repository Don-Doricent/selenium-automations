from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")
#THIS WILL ALWAYS GRAB REAL SEARCH BOX:

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "q"))
)


search_box = driver.find_element(By.NAME, "q")
search_box.clear() 
search_box.send_keys("tech with tim", Keys.RETURN)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim") #LINK_TEXT finds the exact text. 
link.click()

time.sleep(200)

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path = "C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://www.ebay.com/")


element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "viewport")))

print(driver.title)
print(driver.current_url)
pageSource = driver.page_source

searchbox = driver.find_element(By.XPATH, "//*[@id='gh-ac']")

print("Display Status: ", searchbox.is_displayed())
print("Enabled Status: ", searchbox.is_enabled())

# print("Display Status: ", searchbox.is_displayed())


#Test case 1

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path = "C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "nav[aria-label='Sidepanel']")))

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

assert act_title == exp_title

driver.close()


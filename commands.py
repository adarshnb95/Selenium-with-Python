import time
import requests
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

# is_selected: only for radio buttons and checkboxes

searchbox.send_keys("laptop")

driver.find_element(By.ID, "gh-btn").click()

driver.implicitly_wait(5)

checkbox = driver.find_element(By.CSS_SELECTOR, "input[aria-label='16 GB']")

print(checkbox.is_selected()) # should return False

checkbox.click()

checkbox = driver.find_element(By.CSS_SELECTOR, "input[aria-label='16 GB']")
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "description")))

driver.implicitly_wait(5)

# print(checkbox.is_selected())  # should return True


# time.sleep(3)

# ######## Ask Pandey why we need  to reassign checkbox #####################


# #  Navigational commands

# driver.get("https://www.amazon.com")
# time.sleep(3)   #Just to show page -- can be removed

# driver.back()

# time.sleep(3)   #Just to show page -- can be removed

# Checkboxes #

# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@aria-label, 'GB')]")
# print(len(checkboxes))


# ### Not working ###
# for i in range(1, len(checkboxes)):
#     checkboxes[i].click()
#     WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@aria-label, 'GB')]")))

# time.sleep(2)

######### Links ###########

# Get all links

allLinks = driver.find_elements(By.TAG_NAME, 'a')

print(len(allLinks))
# count = 0

# for link in allLinks:
#     url = link.get_attribute('href')
#     try:
#         res = requests.head(url)
#     except:
#         None
    
#     if res.status_code >= 400:
#         print(url, " is a broken link")
#         count += 1
#     else:
#         print(url, " is a valid link")
    
# print("Total broken links on page: ", count)


driver.close()




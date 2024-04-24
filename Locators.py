from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path = "C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://www.ebay.com/")
driver.maximize_window()


element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "viewport")))

sliders = driver.find_elements(By.CLASS_NAME, 'vl-carousel__item')
print(len(sliders))


links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

# driver.find_element(By.CSS_SELECTOR, "input#gh-ac").send_keys("abc")
# driver.find_element(By.ID, "gh-btn").click()


driver.find_element(By.XPATH, "//*[@id='mainContent']/div[1]/div/div[2]/div[3]/div[2]/div/a/div[2]").click()

abc = input("Enter a key to continue")


# Notes for more locators using CSS_SELECTOR
# tag and id                    tagname#valueof ID                                      ex: input#email
# tag and class                 tagname.valueofClass                                    ex: input.inputtext
# tag and attribute             tagname[attribute=value]                                ex: input[data-testid=royal_email]
# tag, class and attribute      tagname.valueofClass[attribute = value]                 ex: input.inputtext[data-testid=royal_email]
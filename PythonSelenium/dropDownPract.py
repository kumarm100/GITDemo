import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.maximize_window()
driver.find_element(by=By.ID, value="autosuggest").send_keys("Ind")
time.sleep(2)
counteries = driver.find_elements(by=By.CSS_SELECTOR,value="li[class='ui-menu-item'] a")

for country in counteries:
    print(country.text)
    if country.text == "India":
        country.click()
        break

print(driver.find_element(by=By.ID, value="autosuggest").text)
assert driver.find_element(by=By.ID, value="autosuggest").get_attribute('value') == "India"

driver.close()

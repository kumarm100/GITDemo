from selenium import webdriver

# Locators :  ID,name,xpath,css,classname,linktext
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.current_url

# driver.find_element(by=By.XPATH, value="//label[contains(text(),'Name')]//following-sibling::input[@name='name']").send_keys("Hello")

driver.find_element(by=By.CSS_SELECTOR,
                    value="#username").send_keys("kumarm100@yahoo.com")
driver.find_element(by=By.CSS_SELECTOR, value=".password").send_keys("test")
driver.find_element(by=By.CSS_SELECTOR, value=".password").clear()
driver.find_element(by=By.LINK_TEXT, value="Forgot Your Password?").click()


driver.find_element(by=By.XPATH, value="//input[contains(@name,'cancel')]").click()
# print(driver.find_element(by=By.CSS_SELECTOR, value="div[class*='alert-success']").text)
# CSS - form[name='login'] label:nth-child(3)
# driver.close()

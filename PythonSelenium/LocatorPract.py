from selenium import webdriver

# Locators :  ID,name,xpath,css,classname,linktext
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.current_url

driver.find_element(by=By.XPATH,
                    value="//label[contains(text(),'Name')]//following-sibling::input[@name='name']").send_keys("Hello")

driver.find_element(by=By.CSS_SELECTOR,
                    value="input[name='email']").send_keys("kumarm100@yahoo.com")
dDown = Select(driver.find_element(by=By.ID, value="exampleFormControlSelect1"))
dDown.select_by_visible_text("Female")
dDown.select_by_index(0)


driver.find_element(by=By.CSS_SELECTOR, value="input[class*='btn-success']").click()


print(driver.find_element(by=By.CSS_SELECTOR, value="div[class*='alert-success']").text)

sMsg = driver.find_element(by=By.CSS_SELECTOR, value="div[class*='alert-success']").text
assert "Succccess" in sMsg

# driver.close()

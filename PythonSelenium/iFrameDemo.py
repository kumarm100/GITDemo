from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=("C:\\Users\\kumar\\Drivers\\chromedriver.exe"))

driver.get("https://the-internet.herokuapp.com/iframe")
# frame id or frame name or index value
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH, "//body[contains(@id,'tinymce')]").clear()
driver.find_element(By.XPATH, "//body[contains(@id,'tinymce')]").send_keys("This is the iframe test")
driver.switch_to.default_content()

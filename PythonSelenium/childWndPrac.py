from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=("C:\\Users\\kumar\\Drivers\\chromedriver.exe"))

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
nodes = driver.window_handles
print(nodes.__len__())
driver.switch_to.window(nodes[1])
print(driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]").text)
driver.close()
driver.switch_to.window(nodes[0])

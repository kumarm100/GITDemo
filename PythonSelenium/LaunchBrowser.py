from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe")
driver = webdriver.firefox(executable_path="C:\\Users\\kumar\\Drivers\\geckodriver.exe")
#driver = webdriver.edge(executable_path="C:\\Users\\kumar\\Drivers\\msedgedriver.exe")
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()

driver.close()

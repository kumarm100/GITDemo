# w3schools.com/js/js_htmldom_document.asp
# Javascript HTML DOM Document
# JS DOM can access any element on the webpage just like how selenium does
# selenium have a method to execute javascript code in it

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()

driver.find_element(By.NAME,"name").send_keys("Hello")
print(driver.find_element(By.NAME,"name").text)
print(driver.find_element(By.NAME,"name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopMenu = driver.find_element(By.CSS_SELECTOR,"a[href*='shop']")
driver.execute_script('arguments[0].click();',shopMenu)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
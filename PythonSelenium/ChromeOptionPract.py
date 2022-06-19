import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\kumar\\Drivers\\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(3)
print(driver.title)
driver.find_element(By.XPATH, "//a[text()='Shop']").click()

productList = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(productList.__len__())
iCnt = productList.__len__()

#for m in range(iCnt):
 #   pName = productList.__getitem__(m).find_element(By.XPATH,"div/h4/a")
  #  if pName.text == "Blackberry":
   #     print(pName.text)
    #    productList.__getitem__(m).find_element("//ancestor::div[1]//following-sibling::div//button").click()

for prod in productList:
    pName = prod.find_element(By.XPATH,"div/h4/a").text
    if pName == "Blackberry":
        prod.find_element(By.XPATH,"div/button").click()
        driver.find_element(By.XPATH,"//div[@id='navbarResponsive']//a").click()
        driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        driver.find_element(By.ID,"country").send_keys("ind")
        waitTime = WebDriverWait(driver,7)
        waitTime.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        action = ActionChains(driver)
        menuItem = driver.find_element(By.LINK_TEXT,"India")
        action.move_to_element(menuItem).click().perform()
        time.sleep(2)
        action.click(driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']//input[@id='checkbox2']")).perform()
        driver.find_element(By.XPATH,"//input[contains(@type,'submit')]").click()
        sMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
        print(sMsg)
        assert "Your order will be delivered in next few weeks" in sMsg
        driver.get_screenshot_as_file("Screen1.png")


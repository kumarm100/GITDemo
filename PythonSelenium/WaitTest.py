from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from re import search

list1 = []
list2 = []

driver = webdriver.Chrome(executable_path=("C:\\Users\\kumar\\Drivers\\chromedriver.exe"))

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.implicitly_wait(5)  # wait until 5 seconds if object is not displayed
# Global wait
# it took 1.5 seconds to reach next page - execution will resume to next object
# if the object do not show up at all,then there is a issue with the
#break
            # wait = WebDriverWait(driver, 3)
            # wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

prodList = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'products')]/div[@class='product']//h4")
addToCart = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'products')]/div[@class='product']//button")
print(prodList.__len__())

for m in range(prodList.__len__()):
    print(prodList[m].text)
    prodName: str = prodList[m].text
    while m < 3:
        print("Inside the if condition ==>>" + prodList[m].text)
        list1.append(prodList[m].text)
        print(list1)
        addToCart[m].click()
        break

driver.find_element(by=By.XPATH, value="//a[@class='cart-icon']").click()
if driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").is_displayed():
    driver.find_element(by=By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()
    beforeDiscount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
    driver.find_element(by=By.XPATH, value="//input[@class='promoCode']").send_keys("rahulshettyacademy")
    driver.find_element(by=By.XPATH, value="//button[text()='Apply']").click()
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoinfo")))
    print(driver.find_element(by=By.CSS_SELECTOR, value="span.promoinfo").text)
    afterDiscount = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text
    totAmt = driver.find_element(By.CSS_SELECTOR, "span.totAmt").text
    selectedProdList = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'products')]//table//td[2]//p")
    print(selectedProdList.__len__())
    for n in range(selectedProdList.__len__()):
        print(selectedProdList[n].text)
        list2.append(selectedProdList[n].text)
sum = 0
Amt = driver.find_elements(by=By.XPATH, value="//div[contains(@class,'products')]//table//td[5]//p")
for a in Amt:
    sum = sum + int(a.text)

print(sum)
assert int(sum) == int(totAmt)

print(list2)
assert list1 == list2

assert float(afterDiscount) < float(beforeDiscount)

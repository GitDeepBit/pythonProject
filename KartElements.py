# Assignment was completed as part of this file. Refer EOF for comments & steps 28, 29, 39, 43, 44, 47, 85, 87 for code

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serobj, options=optobj)

driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")

time.sleep(2)

emptyCart = []
existingCart = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

cartElements = driver.find_elements(By.XPATH, "//div[@class='products']/div")

print(len(cartElements))

assert len(cartElements) > 0

# Fetched the cartElements and their titles then appended the values 1 by 1 inside the emptyCart list
for cartProducts in cartElements:
    emptyCart.append(cartProducts.find_element(By.XPATH, "h4").text)
    cartProducts.find_element(By.XPATH, "div/button").click()

# Here, Printed both the list values
print("Empty cart filled during run time is:", emptyCart)
print("Existing cart is:", existingCart)

# Compared the emptyCart list with existing Cart list to validate that both are same
assert emptyCart == existingCart

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")

sumOf = 0

for price in prices:
    sumOf += int(price.text)

# find_element will only find the element and returns the place of that HTML tag and not the value
# .text is used to fetch the value from the tag
# int to convert the text into integer

totalPrice = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert(sumOf == totalPrice)

print("Total of your order is:", sumOf)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

expWait = WebDriverWait(driver, 10)
expWait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

codeAppliedText = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text

print(codeAppliedText)

assert codeAppliedText == 'Code applied ..!'


# Comparing total order value is > discounted price
valueAfterDiscount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

assert totalPrice > valueAfterDiscount

# Assignment
# Create a list and compare it with a list that will be created during run time by fetching the title of cart elements
# Compare that total order price OR total amount of the order is greater than discounted price when promoCode is applied

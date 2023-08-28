# Waits and Chain-ing of elements
# Implicit Waits are not useful for find_elements, we have to use time.sleep in that case
# driver.implicitly_wait(3)
# expWait = WebDriverWait(driver, 5)
# expWait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo'")))

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

# Definition of implicit waits
# The argument is in "Seconds", it will tell the browser to wait for n seconds when the code runs
# This implicit wait gets applied to each and every line of code present in this file
# Meaning the execution will be slow but if the element is found within, 2 or 3 seconds then
# It won't wait for the remaining time. Here, it is better than time.sleep() because
# time.sleep() will wait no matter the element on the page is found or not
# because it will wait for the same amount of seconds that are given as the arguments
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")

time.sleep(2)

# Implicit waits might not be very useful here because implicit wait will get the list & it will not have any values
# Because during run time the list is returned & it will be empty.
# Empty list will fail our functional code and due to this time.sleep() is useful
# time.sleep() is used here to put wait on browser

cartElements = driver.find_elements(By.XPATH, "//div[@class='products']/div")

print(len(cartElements))

assert len(cartElements) > 0

# We cannot use chaining using cartElements because it contains a list altogether and to make a chaining effect
# We have to select a single value from the list and then traverse
# For example, if we use cartElements.find_element - it won't show anything to us

for cartProducts in cartElements:
    # Chaining mechanism: where the single element value is used to chain further, creating a chained XPATH to traverse
    cartProducts.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit waits
# WebDriverWait is a class which takes driver as the first argument and second argument as the number of seconds
# .until(expected_conditions) is a way to wait and fetch the element based on a condition
# until is for waiting part and expected conditions is to give a condition
# expected_conditions. is having a different set of conditions based on which we can tell the browser to wait
# conditions like presence_of_element_located etc. takes find_element argument structure
# this is similar to switch_to.alert
# And alert.text etc.

expWait = WebDriverWait(driver, 10)
expWait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

codeAppliedText = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text

print(codeAppliedText)

assert codeAppliedText == 'Code applied ..!'


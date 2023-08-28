import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser, options=opo)

driver.get("https://rahulshettyacademy.com/angularpractice/")

assert(driver.current_url == "https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.LINK_TEXT, "Shop").click()
# Regular expression in CSS
# driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

# Regular expression in XPATH
driver.find_element(By.LINK_TEXT, "Shop").click()
# driver.find_element(By.XPATH, "//a[contains(@href,'shop')]") - This is not working for me

# assert(driver.current_url == "https://rahulshettyacademy.com/angularpractice/shop")

# Chain from parent, so create a parent XPATH instead of child XPATH
# productElements = driver.find_elements(By.XPATH, "//h4/a")

driver.implicitly_wait(5)
productElements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# Traversing the products and selecting 1
for product in productElements:
    if product.find_element(By.XPATH, "div/h4/a").text == 'Samsung Note 8':
        product.find_element(By.XPATH, "div/button").click()

# Checkout - This line is failing for no reason
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

# -------------------------------->EXTRA CODE<-------------------------------- #
# Will try this later
# Validate the names in the cart, here we have 1 element but what if we have more than 1
# cartElements = driver.find_elements(By.XPATH, "//tr/div/h4/a")

# for cartProduct in cartElements:
# if cartProduct.text in ("Samsung Note 8", "Nokia Edge"):
# print(cartProduct.text)

# -------------------------------->EXTRA CODE<-------------------------------- #

# Checking out from cart page
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("Ind")

# Implicit waits won't work here
explicitWait = WebDriverWait(driver, 10)
explicitWait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

# Checking the checkbox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# Purchase Button
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Fetching the success message
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successMessage


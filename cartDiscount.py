z`import time

from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)
# Implicit wait: Having this wait time for each and every line/code in the script
driver.implicitly_wait(5)
name = "Deep"

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
# This cannot be commented/removed as we have used implicit wait on line 18
# and implicit wait will not help in case of returning results within a list
# We will have to use "time.sleep()", when we are getting list values in return
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # Here we are returning list
count = len(results)
assert count > 0

for result in results:
    # Chain mechanism: As we have used result variable to traverse more into the tags
    productText = result.find_element(By.XPATH, "h4").text
    print(productText)
    # Chain mechanism: As we have used result variable to traverse more into the tags
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5) # This can be commented as we have used implicit wait on line 18
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5) # This can be commented as we have used implicit wait on line 18
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


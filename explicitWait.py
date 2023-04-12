import time

from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
print(results)
count = len(results)
assert count > 0

sListValues = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
# dListValues = []

# Another way but it is doing same thing as below loop
# for svalue in results:
    #dListValues.append(svalue.find_element(By.XPATH, "h4").text)

for result in results:
    # Chain mechanism: As we have used result variable to traverse more into the tags
    # dListValues.append(result.find_element(By.XPATH, "h4").text)
    assert result.find_element(By.XPATH, "h4").text in sListValues
    # productText = result.find_element(By.XPATH, "h4").text
    # print(productText)
    # Chain mechanism: As we have used result variable to traverse more into the tags
    result.find_element(By.XPATH, "div/button").click()

# assert dListValues == sListValues

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Summation for Total
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

# time.sleep(5) # This can be commented as we have used implicit wait on line 18
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5) # This can be commented as we have used implicit wait on line 18

# Below two lines are explicit wait and this overrides implicit wait.
# First line defines the wait time for webDriver
# Second line fetches the element for which it has to wait
wb = WebDriverWait(driver, 10)
wb.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

if float(driver.find_element(By.CLASS_NAME, "discountPerc").text[:-1]) <= 0:
    raise Exception("Discount not applied")

assert discountAmount < totalAmount

# When we have

# Alternate: Do not define discountAmount
# assert int(driver.find_element(By.CLASS_NAME, "discountAmt").text) < totalAmount




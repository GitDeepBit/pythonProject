# CSSSelector = (By.CSS_SELECTOR, "#ID") OR (BY.CSS_SELECTOR, ".className")
# XPATH = (BY.XPATH, "(//tagName=[@attribute='value'])[appearance or index]") -> Appearance or index, refer line 47

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/angularpractice")

assert(driver.current_url == "https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("dsm.deep97@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password123")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name=name]").send_keys("Deep Singh Modi")

# We can use #ID or .className
# #ID is used in CSS Selector when there is an id attribute & we want to make it unique
# .className is used in CSS Selector when there is a class attribute & we want to make it unique
# Here, #ID is the value present against id attribute in the tag
# Same goes for the class name as well, class attribute holding value i.e. class name
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

# This is a new way to traverse a particular field using XPATH where XPATH is also common across the page
# Meaning there are n number of fields which can be accessed using the following XPATH:- //input[@type='text']
# But to access a particular field based on its occurrence on the page we have used indexing
# Here, [3] represents that it is 3RD FIELD on the page, starting from TOP LEFT of the page & we want to access it
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Overriding")

# Clearing the field using ".clear() method" as this is a twin field on the page which takes value from line 29
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

print(message)

assert 'Success' in message

driver.close()

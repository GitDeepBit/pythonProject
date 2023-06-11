# ID, NAME, find_elements, send_keys, click

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/angularpratice/")

assert(driver.current_url == "https://rahulshettyacademy.com/angularpratice/")

# LOCATORS
# ID, NAME, CLASSNAME, LINKTEXT, XPATH, CSSSelector

# Here find_element will be used to fetch the field using locators that is property of the fields, class, name, id etc
# Send keys helps us to send information to that particular field
driver.find_element(By.NAME, "email").send_keys("dsm.deep97@gmail.com")

# Same as above comment, here we have used ID locator instead of NAME locator
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password123")

# In case of fields that requires a click, we use click function. It depends on the type of field we are using
driver.find_element(By.ID, "exampleCheck1").click()

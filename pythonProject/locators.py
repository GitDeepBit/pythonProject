from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locators available in python
# ID, NAME, Xpath, CSSSelector, ClassName, linkText
driver.find_element(By.NAME, "email").send_keys("dsm.deep97@gmail.com")  # send_keys is used to send data
driver.find_element(By.ID, "exampleInputPassword1").send_keys("hello123")
driver.find_element(By.ID, "exampleCheck1").click()  # click is used to click any button

# CSS - tagName[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Deep Singh Modi")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Select tag for static picklist values
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
# dropdown.select_by_value("any value present on select tags")

# XPATH - //tagName[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text  # We can access elements by className
print(message)

# how to make XPATH unique to a tag using a property
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

assert "Success" in message


#  Types of XPATH
# //tagName
# //tagName[@attribute='value']
# (//tagName[@attribute='value'])[3]

#  Types of CSS Selector
#  #id or .className

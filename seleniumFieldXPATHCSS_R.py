# XPATH, CSS
# ***IMP****
# Whenever using Class as an attribute in XPATH, make sure to use all the values of the class attribute
# otherwise it won't work. For eg, class attribute had 4 class names as values then passing only 1 value will
# fail the code. **This can work only when we are using CSSSelector or ClassName**
# ***IMP****

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

# By.NAME
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password123")

# By.ID
driver.find_element(By.ID, "exampleCheck1").click()

# By.CSSSelector
# tagName[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Deep Singh Modi")

# By.XPATH
# //tagName[@attribute='value']
# Here, the field that we are trying to access is a Button, so we are using .click() [Submit button on the page]
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Here, we are getting the text present on the element using .text property
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
# OR driver.find_element(By.CLASS_NAME, "alert-success") - Another Syntax

# assert(message == "Success! The Form has been submitted successfully!.")
assert 'Success' in message

# Printing the message which is grabbed in line 38
print(message)

driver.close()
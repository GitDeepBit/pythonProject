from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)
name = "Deep"

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# To switch the control from web browser to alert PopUp Window, we use this
alertbox = driver.switch_to.alert

# In Selenium we do not have anything specific for popup windows, so we use this function
alertBoxText = alertbox.text # Fetching alert box text

print(alertBoxText) # Printing the alertBox Text
# alertbox.dismiss()

assert name in alertBoxText
alertbox.accept()

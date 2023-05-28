import time

from selenium import webdriver  # Imported WebDriver
# The above line imports the webdriver class FROM selenium package

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service
# Imported Class: Service
# To invoke chrome we have to use chrome driver
# Service class object will take chrome driver's location present in the system
# Service class' object will be passed as an argument in webdriver class' object

options_obj = Options()
options_obj.add_experimental_option("detach", True)

# Object name = ClassName(args)
service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver object and invoked service and options object. This invokes the browser
# Object name = ClassName.function(parameter = obj)
driver = webdriver.Chrome(service=service_obj, options=options_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise")

assert(driver.current_url == "https://rahulshettyacademy.com/dropdownsPractise/")

print(driver.title)  # Title here is a property

print(driver.current_url)

driver.close()

# Webdriver object needs service class's object to invoke browser's driver
# Browser's driver can be invoked via web driver application
# Web driver application can be fetched via service class' object
# So, web driver application path will be passed as argument in service class object
# This WAY:
# Service class object will invoke the driver application which in turn will invoke the browser
# This way we will get the control of the first browser/browser window using webdriver's object






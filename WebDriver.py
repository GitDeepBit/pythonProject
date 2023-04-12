from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service

options_obj = Options()
options_obj.add_experimental_option("detach", True)  # Called this function to keep the window open

#  Assigned the chromedriver.exe to Service object to invoke service object
service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

# Firefox driver: geckodriver
# Edge driver: msedgedriver

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)

# Maximise the window
driver.maximize_window()

#  Called a specific URL using get method
driver.get("https://www.youtube.com")

print(driver.title)  # It fetches the title of the site

print(driver.current_url)  # It returns URL

driver.get("https://www.google.com")

#  driver.minimize_window()

driver.back()
driver.refresh()
driver.forward()
import time

from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise")

driver.find_element(By.ID, "autosuggest").send_keys("ia")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for count in countries:
    print(count.text)

for country in countries:
    if country.text == "India":
        country.click()
        # print(country)
        break

# print(driver.find_element(By.ID, "autosuggest").text)

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

driver.close()

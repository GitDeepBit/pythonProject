# Dynamic text, how to capture dynamic text value and how to validate it or print it

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

assert(driver.current_url == "https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")

# Here we are making the browser to hold for some time, so that options can appear & we can select them
time.sleep(2)

# Here, find elements will fetch all the results in a list
# find_elements will capture all the elements[values] at once instead of taking 1 value at a time
dropDownList = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

# This will return len of the list OR length of elements captured via browser's drop down list field
print(len(dropDownList))

# We are travesing the lists and checking if it is India then we are clicking on it and printing it
for country in dropDownList:
    if country.text == "India":
        country.click()
#  Here, country became dropDownList and that is why we were able to use the click operation
        print(country.text)
        break

# We have added a break statement as the loop should break when the match is found
# And should not traverse the list items further. This will save the memory and help us execute the code faster


# Here, get.attribute is used because the values are not present on the page when the page is loaded
# The value for "auto suggest" field appears when we send the values via selenium script
# Due to this, we cannot get the value of the dynamic field by using .text instead
# we have to use get.attribute("value")
# Here, "value" represents that any value that is selected via the code and now present on the page dynamically
# will be taken into consideration by the HTML DOM and won't require "Value" attribute for the field explicitly
if driver.find_element(By.ID, "autosuggest").get_attribute("value") == "SIndia":
    print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
else:
    print("Value selected is not matched")

# OR

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
print("Value selected from dynamic dropdown is:", driver.find_element(By.ID, "autosuggest").get_attribute("value"))

driver.close()
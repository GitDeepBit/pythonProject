# Here, we are sorting the table by clicking on a button which is table column header, Step 28
# Capturing the elements on the table from the first column using "for" loop and storing it in browserVeggies
# Before sorting out the browserVeggies from the Selenium code ( Not the browser or element which is already done )
# Storing it inside a new list which will depict our original list i.e. originalVeggies
# Now, Sorting browserVeggies via selenium code in Step 36
# Comparing the originalVeggies to newly sorted browserVeggies
# This seems useless. But we are doing this to check if the sorting is happening in the beginning or not
# Like if there was an issue while clicking on the table column header button. Did it sort the list or not?

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser, options=opo)

browserDefaultVeggies = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Here, we sorted the column by clicking the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieListElements = driver.find_elements(By.XPATH, "//tr/td[1]")

# veggieList is iterating web elements and not text, so veggie list itself a web element and not list
for veggie in veggieListElements:
    browserDefaultVeggies.append(veggie.text)

# Copying the list using copy of the list. In previous version, we used to have slice
# Sorted list is getting copied
originalVeggies = browserDefaultVeggies.copy()

# sorting browserDefaultVeggies List
browserDefaultVeggies.sort()

assert originalVeggies == browserDefaultVeggies

# Before Line 31, we can fail the code by using debugger and manually interrupting the flow in between via debugger
# Manual intervention would be clicking the header column again
# This way assert will fail because list won't be sorted

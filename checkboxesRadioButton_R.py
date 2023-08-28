# Checking is_displayed as well as part of this file
# assert and assert not

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

assert(driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/")

checkBoxList = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Here, "value" represents that if the value attribute is present inside the tag will be used
for checkbox in checkBoxList:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        # assertions for checkboxes
        assert checkbox.is_selected()
        print("Checkbox is selected and the option is:", checkbox.get_attribute("value"))
        break

radioButtonList = driver.find_elements(By.XPATH, "//input[@class='radioButton']")

for radioButton in radioButtonList:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        # assertions for radio buttons
        assert radioButton.is_selected()
        print("Radio Button is select and the radio button is:", radioButton.get_attribute("value"))
        break

# Checking if a section is displayed or not
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# Hiding it using a button which hides a displayed area/tag/content by clicking it
driver.find_element(By.ID, "hide-textbox").click()

# Checking "if it is not displayed" instead of "checking it is displayed" using not keyword
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# Displaying the area/tag/content again
driver.find_element(By.ID, "show-textbox").click()

# Checking if it is displayed or not
assert driver.find_element(By.ID, "displayed-text").is_displayed()

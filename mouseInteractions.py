from sys import path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser, options=opo)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert(driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
driver.maximize_window()
# ActionChains class is used to perform numerous amount of mouse actions like Hover, right click , click & hold etc.
action = ActionChains(driver)

# Double click
# All methods under action class will take driver.find_element as argument - Refer line 36
# action.double_click()

# Drag and Drop - Drag will be a source element on the page, Drop will be a target element on the page
# action.drag_and_drop(source,target)

# Click on hold
# action.click_and_hold()

# Move to an element
# .perform() or PERFORM is used to execute the mouse action completely
# perform completes the purpose of action class methods
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# Right click
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

# Moving to a certain element and performing an action
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).perform()

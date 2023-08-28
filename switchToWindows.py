from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=ser, options=opt)

driver.get("https://the-internet.herokuapp.com/windows")

assert(driver.current_url == "https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

# This codes captures all the windows opened by Selenium and creates a list/array
windowsOp = driver.window_handles

# driver.switch_to is used to switch to a window & we are passing window handles object to fetch the list of windows
# Window handles object is taking index as the argument, indexing starts with 0
driver.switch_to.window(windowsOp[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

# Switching back to first window
driver.switch_to.window(windowsOp[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


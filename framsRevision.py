from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=ser, options=opt)

driver.get("https://the-internet.herokuapp.com/iframe")

assert(driver.current_url == "https://the-internet.herokuapp.com/iframe")

# Switching to Frames, Frame takes either ID or Name as the argument
driver.switch_to.frame("mce_0_ifr")

# Accessing data within frames and clearing it
driver.find_element(By.ID, "tinymce").clear()

# Sending keys to the same locator
driver.find_element(By.ID, "tinymce").send_keys("New Content updated by Automated code")

# Switching back to Default browser screen from frames
driver.switch_to.default_content()

# Printing browser's content
print(driver.find_element(By.CSS_SELECTOR, "h3").text)




from selenium import webdriver  # Imported WebDriver

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)
# Implicit wait: Having this wait time for each and every line/code in the script
driver.implicitly_wait(5)

# Opening loginPage
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# Switching our control to frames which are part of HTML code by not locally
# Meaning they are present as part of the HTML web page but their existence is solely on their own
driver.switch_to.frame("mce-0-ifr")

# For clearing any data
driver.find_element(By.ID, "tinymce").clear()

# For sending information
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frame")

# For switching back to original content/window which was opened for the first time
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
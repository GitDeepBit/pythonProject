from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/client")

# assert(driver.current_url == "https://rahulshettyacademy.com/client")

# LINK_TEXT is used for anchor tags
# The value is the text present in the anchor tag which is Forgot password? and
# We can use another similar locator which is "PARTIAL_LINK_TEXT" but this can pick any value which partially matches
# So, either use your values in a way that it matches a particular value only OR try not to use it
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# XPATH Traversing Parent-Child
# Traversing the element/tag using parent-child locator relationship OR Top2Bottom approach
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

# CSSelector Traversing Parent-Child
# Traversing the element/tag using parent-child locator relationship OR Top2Bottom approach
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(1) input").send_keys("Hello@1234")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Another way to click on the button

driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

driver.close()

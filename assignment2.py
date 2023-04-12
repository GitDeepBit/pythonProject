import time

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
driver.get("https://rahulshettyacademy.com/loginpagePractise")
# Maximizing the login page
driver.maximize_window()

# Opening a new window using anchor tag's Link Text
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# Switching to new window using windowHandles which returns a list
windowsOpened = driver.window_handles
# Using index as 1 because the index of first window will be [0]
driver.switch_to.window(windowsOpened[1])

# Fetching the text from second window
websiteText = driver.find_element(By.XPATH, "//p[@class='im-para red']/strong").text
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]

# Closing window
driver.close()

# Switching the control to previous window
driver.switch_to.window(windowsOpened[0])

# Fetching id and password
driver.find_element(By.ID, "username").send_keys(websiteText)
driver.find_element(By.ID, "password").send_keys("123456")

# Clicking on button
driver.find_element(By.ID, "signInBtn").click()

# This is explicit wait timer
wb = WebDriverWait(driver, 10)
# Wait until the desired text is found

# This is checking if the element is visible on the page or not
# Presene checks for its present & it might stay on the page
wb.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# Below code will only take code within the tag and here there is only one sentence and tag inside this tag
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

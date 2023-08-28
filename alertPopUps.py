from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

name = "Deep Singh Modi"

driver.get("https://rahulshettyacademy.com/AutomationPractice")

assert(driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/")

# Lecture code: driver.find_element(By.CSS_Selector, "#name").send_keys(name)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys(name)

# Lecture code: driver.find_element(By.ID, "alertbtn").click()
driver.find_element(By.ID, "alertbtn").click()

# Switch to will switch the drivers control to a desired page/location/window etc.
# switch_to has various options: alert, window, frame, new window, parent frame etc.

# Switch from browser to different mode, here switch_to is used to switch to alert mode
# switch_to.alert will finally switch the control to alert window
alert = driver.switch_to.alert

# .text on alert will help us grab the text present in the alert window
alertText = alert.text

print(alertText)

assert "Deep Singh Modi" in alert.text

# Accepts means click on "OK" button
# alert.accept(); commenting this as the code is running way too fast

# Dismiss means click on "Cancel" button
# alert.dismiss()

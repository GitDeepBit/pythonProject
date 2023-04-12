from selenium import webdriver  # Imported WebDriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options  # Imported Class: Options

from selenium.webdriver.chrome.service import Service  # Imported Class: Service
from selenium.webdriver.common.by import By

options_obj = Options()
options_obj.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

#  Created Driver objected and invoked service and options object. This invokes the browser
driver = webdriver.Chrome(service=service_obj, options=options_obj)
driver.implicitly_wait(5)


driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles  # This returns windows opened via automation in a list starting with index 0
driver.switch_to.window(windowsOpened[1])  # Switch_to is used to switch windows or tab

print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()  # If more than 1 tab is opened, it will close the tab on which we have the driver's control [Ctrl + W]
# Even if we close the current window, the control will still be on this window which will be undefined
# As the window is already closed
driver.switch_to.window(windowsOpened[0])  # We have to use switch_to if we are closing the previous window or moving
# Our control to new window
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
print(driver.find_element(By.TAG_NAME, "h3").text)
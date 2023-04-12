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


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
#action.double_click(driver.find_elements).perform()
#action.context_click().perform()  Right clicking the element
#action.drag_and_drop().perform() Draging one element from source to destination
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

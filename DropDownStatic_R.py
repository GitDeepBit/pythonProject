# Static dropdown values can be accessed using select() class
# We will pass driver.find_element inside Select() class

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com/angularpractice")

assert(driver.current_url == "https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("dsm.deep97@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password123")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name=name]").send_keys("Deep Singh Modi")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")

# Select for Static drop down
# Static Drop Down

dropDown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropDown.select_by_index(1)  # Selects Female
dropDown.select_by_visible_text("Male")

# dropDown.select_by_value("")  # This will work only when there is a value attribute in the tag

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Overriding")

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

print(message)

assert 'Success' in message

driver.close()

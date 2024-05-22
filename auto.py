import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://www.theTestingWorld.com/testings")

driver.maximize_window()

driver.find_element(By.NAME, "fld_username").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='myusername@gmail.com']").send_keys("Vikas@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("vikas1234")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Confirm password']").send_keys("vikas1234")
time.sleep(2)
driver.find_element(By.ID, "datepicker").send_keys("29/09/1999")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Phone']").send_keys("9371548876")
time.sleep(2)
driver.find_element(By.NAME, "address").send_keys("1-24,JHN,APPPLY WROD,NITHO,8743")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='office']").click()
time.sleep(2)
obj1 = Select(driver.find_element(By.NAME, "sex"))
obj1.select_by_visible_text("Male")
time.sleep(2)
obj1 = Select(driver.find_element(By.ID, "countryId"))
obj1.select_by_visible_text("Inida")
time.sleep(2)
obj1 = Select(driver.find_element(By.ID, "stateId"))
obj1.select_by_visible_text("Telangana")
time.sleep(2)
obj1 = Select(driver.find_element(By.ID, "cityId"))
obj1.select_by_visible_text("Hyderabad")
time.sleep(2)
driver.find_element(By.NAME, "zip").send_keys("8346")
time.sleep(2)
driver.find_element(By.XPATH, "//h2[normalize-space()='Terms and Conditions']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Sign up']").click()

time.sleep(6)






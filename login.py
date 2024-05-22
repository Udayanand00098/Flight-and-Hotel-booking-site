import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("http://shop.thetestingworld.com/")
"""

driver.find_element(By.XPATH, "//label[normalize-space()='Login']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Vikas")

driver.find_element(By.XPATH, "//input[@placeholder='mypassword']").send_keys("vikas123")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(6)
"""
driver.quit()



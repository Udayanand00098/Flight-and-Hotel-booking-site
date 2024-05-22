
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")

driver.find_element(By.XPATH,"//a[@id='login_Layer']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys("chintalapalliudayanannd@gmail.com")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Qwerty@1234")
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(6)

"""
driver.find_element(By.XPATH, "//em[@class='icon edit']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

driver.find_element(By.XPATH, "//button[@id='saveBasicDetailsBtn']").click()

time.sleep(3)
"""

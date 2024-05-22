import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoFindElementByIDandName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.TAG_NAME,'Input').send_keys("auday7138@gmail.com")
        time.sleep(4)
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(6)
        driver.find_element(By.XPATH, "//input[@id='login-password']").send_keys("Qwerty@123")
        time.sleep(6)
        driver.find_element(By.ID, "login-submit-btn").click()
        time.sleep(6)


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()

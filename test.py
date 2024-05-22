
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the Gmail login page
url = "https://accounts.google.com/"

# Your Gmail username and password
username = "auday7138@gmail.com"
password = "Qwerty@#$123"

# Initialize a Chrome WebDriver instance
driver = webdriver.Chrome()

# Open the Gmail login page
driver.get(url)

# Wait for the page to fully load and find the email input field
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)

# Enter the email address and submit
email_field.send_keys(username)
email_field.send_keys(Keys.RETURN)

# Wait for the password input field to be visible and interactable
password_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "password"))
)

# Enter the password and submit
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Once logged in, you can perform further actions on the Gmail page using the driver

# Close the browser
driver.quit()
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these values with your actual credentials
username = "auday7138@gmail.com"
password = "Qwerty@#$123"

# URL of the Gmail login page
login_url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&emr=1&ltmpl=default&ltmplcache=2&osid=1&passive=true&rm=false&scc=1&service=mail&ss=1&ifkv=AaSxoQy2RRH1V7IK1QT2OLbDiFtyySSPj34dGescDIYgxZAMxrYtWiqZc768eSYw43tnvDx5kTTA&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

# Initialize Chrome WebDriver with options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")  # This option can help with headless mode
chrome_options.headless = True

# Create a new Chrome session
driver = webdriver.Chrome(options=chrome_options)

# Open the Gmail login page
driver.get(login_url)

# Fill in the email field using JavaScript
driver.execute_script("document.getElementById('identifierId').value = '{}'".format(username))

# Click on the Next button for email
driver.execute_script("document.getElementById('identifierNext').click()")

# Wait for the password field to appear
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

# Fill in the password field using JavaScript
driver.execute_script("document.getElementsByName('password')[0].value = '{}'".format(password))

# Click on the Next button for password
driver.execute_script("document.getElementById('passwordNext').click()")

print("Logged in Successfully")
"""
from selenium import webdriver

url = "https://www.python.org/"

driver = webdriver.Chrome()

driver.get(url)

title = driver.title

print(title)



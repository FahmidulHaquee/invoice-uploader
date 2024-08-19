import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv(override=True)

DRIVER_PATH=os.getenv("DRIVER_PATH")
PROFILE_PATH=os.getenv("PROFILE_PATH")
UPLOAD_URL=os.getenv("UPLOAD_URL")
USERNAME=os.getenv("UPLOAD_LOGIN_USERNAME")
PASSWORD=os.getenv("UPLOAD_LOGIN_PASSWORD")

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={PROFILE_PATH}")
chrome_options.add_argument(f"profile-directory=Default")

service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Opening the website...")
    driver.get(UPLOAD_URL)
    print("Website opened successfully!")

    email_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "user_login[email]"))
    )
    email_input.send_keys(USERNAME)
    print("Email entered successfully!")
    time.sleep(2)

    password_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "user_login[password]"))
    )
    password_input.send_keys(PASSWORD)
    print("Password entered successfully!")
    time.sleep(2)

    password_input.send_keys(Keys.RETURN)
    print("Form submitted successfully!")
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
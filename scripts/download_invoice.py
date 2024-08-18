from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()
driver_path = os.getenv("DRIVER_PATH")
profile_path = os.getenv("PROFILE_PATH")
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={profile_path}")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com/login")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")

    password_field.send_keys(Keys.RETURN)

    # wait for a certain element to appear
    success_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "success-element-id"))
    )
    print("Login successful!")

finally:
    driver.quit()

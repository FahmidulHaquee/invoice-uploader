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
DOWNLOAD_URL=os.getenv("DOWNLOAD_URL")
USERNAME=os.getenv("DOWNLOAD_LOGIN_USERNAME")
PASSWORD=os.getenv("DOWNLOAD_LOGIN_PASSWORD")

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={PROFILE_PATH}")
chrome_options.add_argument(f"profile-directory=Default")

service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Opening the website...")
    driver.get(DOWNLOAD_URL)
    print("Website opened successfully!")
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "top-header-btn"))
    )
    print("Button loaded successfully!")
    button.click()
    time.sleep(5)
    print("Button clicked successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

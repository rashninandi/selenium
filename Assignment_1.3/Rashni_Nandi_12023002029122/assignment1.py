import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Initialize Browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Set up Explicit Wait
wait = WebDriverWait(driver, 10)

# -------------------------------------------------------------
# 1. By.ID -> Username Field (Fixed function name below)
# -------------------------------------------------------------
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("tomsmith")
print("Successfully located Username field using By.ID")
time.sleep(2)

# -------------------------------------------------------------
# 2. By.NAME -> Password Field
# -------------------------------------------------------------
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
print("Successfully located Password field using By.NAME")
time.sleep(2)

# -------------------------------------------------------------
# 3. By.CLASS_NAME -> Login Button
# -------------------------------------------------------------
login_btn = driver.find_element(By.CLASS_NAME, "radius")
print("Successfully located Login button using By.CLASS_NAME")
time.sleep(2)

# -------------------------------------------------------------
# 4. By.TAG_NAME -> Page Header (h2)
# -------------------------------------------------------------
header = driver.find_element(By.TAG_NAME, "h2")
print(f"Successfully located Header using By.TAG_NAME: '{header.text}'")
time.sleep(2)

# -------------------------------------------------------------
# 5. By.LINK_TEXT -> Footer Link
# -------------------------------------------------------------
footer_link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print(f"Successfully located Link using By.LINK_TEXT: '{footer_link.text}'")
time.sleep(2)

# Click the login button to complete the interaction demo
login_btn.click()
time.sleep(3)

driver.quit()
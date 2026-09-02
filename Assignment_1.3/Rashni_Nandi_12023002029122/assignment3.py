import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1. Standard CSS Selector (ID: #id_value)
username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#username")))
username.send_keys("tomsmith")
print("1. Located Username using ID CSS Selector (input#username)")
time.sleep(2)

# 2. CSS Wildcard Selector: Starts With (^=)
password = driver.find_element(By.CSS_SELECTOR, "input[name^='pass']")
password.send_keys("SuperSecretPassword!")
print("2. Located Password using 'Starts With' Wildcard (input[name^='pass'])")
time.sleep(2)

# 3. CSS Wildcard Selector: Contains (*=)
login_btn = driver.find_element(By.CSS_SELECTOR, "button[class*='radi']")
print("3. Located Login Button using 'Contains' Wildcard (button[class*='radi'])")
time.sleep(2)

# 4. CSS Wildcard Selector: Ends With ($=) - Fixed to target 'com/'
footer_link = driver.find_element(By.CSS_SELECTOR, "a[href$='com/']")
print(f"4. Located Link using 'Ends With' Wildcard (a[href$='com/']): '{footer_link.text}'")
time.sleep(2)

# Click login button using CSS Selector
login_btn.click()
time.sleep(3)

driver.quit()
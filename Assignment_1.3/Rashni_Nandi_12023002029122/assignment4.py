import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# -------------------------------------------------------------
# 1. Direct Child Selector (>)
# Locate <label> directly inside <div class="large-6">
# -------------------------------------------------------------
username_label = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.large-6 > label[for='username']"))
)
print(f"1. Located Username Label via Direct Child Selector (>): '{username_label.text}'")

# Direct child selector to target <input> inside <div class="large-6">
username_input = driver.find_element(By.CSS_SELECTOR, "div.large-6 > input#username")
username_input.send_keys("tomsmith")
time.sleep(2)

# -------------------------------------------------------------
# 2. Descendant Selector (Space)
# Locate <input> nested anywhere inside <form id="login">
# -------------------------------------------------------------
password_input = driver.find_element(By.CSS_SELECTOR, "form#login input#password")
password_input.send_keys("SuperSecretPassword!")
print("2. Located Password Input via Descendant Selector (space)")
time.sleep(2)

# -------------------------------------------------------------
# 3. Direct Child Selector for Button (>)
# Locate <button> directly inside <form id="login">
# -------------------------------------------------------------
login_btn = driver.find_element(By.CSS_SELECTOR, "form#login > button[type='submit']")
print("3. Located Submit Button inside <form> via Direct Child Selector (> pattern)")
time.sleep(2)

# Click the nested button
login_btn.click()
time.sleep(3)

# -------------------------------------------------------------
# 4. Nested Child Selector on Success Page
# Locate <h2> heading inside <div class="example">
# -------------------------------------------------------------
success_heading = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.example > h2"))
)
print(f"4. Located Heading on Success Page via Child Selector: '{success_heading.text}'")

time.sleep(2)
driver.quit()
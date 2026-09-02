import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Initialize Browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

# Set up Explicit Wait
wait = WebDriverWait(driver, 10)

# -------------------------------------------------------------
# STEP 1: Wait for links to load and fetch ALL link elements
# -------------------------------------------------------------
wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))

# find_elements returns a Python list of ALL <a> tags on the page
all_links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total links found on the webpage: {len(all_links)}")
print("=" * 60)

# -------------------------------------------------------------
# STEP 2: Iterate through the list and print text + href URL
# -------------------------------------------------------------
count = 1
for link in all_links:
    link_text = link.text.strip()
    link_url = link.get_attribute("href")
    
    # Print links that have visible text
    if link_text:
        print(f"Link #{count}: {link_text} ---> {link_url}")
        count += 1

print("=" * 60)
print(f"Successfully processed {count - 1} visible links!")

time.sleep(3)
driver.quit()
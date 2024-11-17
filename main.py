import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# set up Web Driver
driver = webdriver.Chrome()
driver.maximize_window()

# opne YoungLA
driver.get("https://www.youngla.com/collections/new-launch")

# get the product you want
# Locate the product by image alt attribute
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='5144 - UFC™ Tracksuit Jackets']")))
product = driver.find_element(By.CSS_SELECTOR, "[alt='5144 - UFC™ Tracksuit Jackets']")
driver.execute_script("arguments[0].click();", product)
# select large
# Wait for the "Large" size option (label with <span>Large>) to be clickable
large_size_label = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[span[text()='Large']]"))
)

driver.execute_script("arguments[0].click();", large_size_label)

# Wait for the 'Add to Cart' button to be clickable
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "button--outline"))
)

# Click the 'Add to Cart' button
add_to_cart_button.click()

# Step 4: Proceed to Checkout
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "cart-drawer__button-price"))
)
# Click the checkout button
checkout_button.click()



# do shipping details
# Wait for the shipping form fields to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)

# Fill in shipping details
email = driver.find_element(By.ID, "email")
email.send_keys("cidthekid0@gmail.com")

first_name = driver.find_element(By.NAME, "firstName")
first_name.send_keys("Cid")

last_name = driver.find_element(By.NAME, "lastName")
last_name.send_keys("Cid")

address1 = driver.find_element(By.NAME, "address1")
address1.send_keys("10944 Duncan Avenue")

city = driver.find_element(By.NAME, "city")
city.send_keys("Lynwood")

postalCode = driver.find_element(By.NAME, "postalCode")
postalCode.send_keys("90262")

phone = driver.find_element(By.NAME, "phone")
phone.send_keys("4243501572")

cardNumber = driver.find_element(By.ID, "number")
cardNumber.send_keys("374245455400126")

# Find the expiry field and input expiration date (MM/YY format)
expiry_field = driver.find_element(By.ID, "expiry")
expiry_field.send_keys("1224")  # Example expiration date (MM/YY format)

cvv_field = driver.find_element(By.ID, "verification_value")
cvv_field.send_keys("091")  # Example CVV code

input("Press Enter to close the browser...")
driver.quit()
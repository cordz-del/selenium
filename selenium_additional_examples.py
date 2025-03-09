from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# Interacting with a checkbox
checkbox = driver.find_element(By.ID, "checkbox_id")
checkbox.click()

# Interacting with a radio button
radio_button = driver.find_element(By.ID, "radio_id")
radio_button.click()

# Interacting with a dropdown
dropdown = driver.find_element(By.ID, "dropdown_id")
dropdown.click()
option = driver.find_element(By.XPATH, "//option[@value='option_value']")
option.click()

# Navigating through multiple pages
driver.get("https://example.com/page1")
driver.get("https://example.com/page2")

# Handling an alert
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# Using implicit wait
driver.implicitly_wait(10)

# Using fluent wait
fluent_wait = WebDriverWait(driver, 10, poll_frequency=1)
element = fluent_wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Close the browser
driver.quit()

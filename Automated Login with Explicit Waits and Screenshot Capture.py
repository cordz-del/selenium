from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("https://example.com/login")  # Replace with the actual login URL
    
    # Set up an explicit wait
    wait = WebDriverWait(driver, 10)
    
    # Wait for the username and password fields to be visible
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    
    # Input credentials (replace with valid credentials)
    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    
    # Find and click the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Wait for the welcome message to appear as confirmation of login
    welcome_message = wait.until(EC.presence_of_element_located((By.ID, "welcome-message")))
    print("Login Successful. Welcome message:", welcome_message.text)
    
    # Take a screenshot of the logged-in page
    driver.save_screenshot("login_success.png")
    print("Screenshot saved as login_success.png")
finally:
    driver.quit()

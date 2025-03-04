from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver (ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

try:
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Find the search box element by its name attribute and input a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Wait until search results are present (up to 10 seconds)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    
    # Retrieve and print the titles of search results
    results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    for index, result in enumerate(results, start=1):
        print(f"Result {index}: {result.text.splitlines()[0]}")
finally:
    driver.quit()

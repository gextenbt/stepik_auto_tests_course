from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# instruct WebDriver to wait for all elements for 5 seconds
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
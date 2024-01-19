from os import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

try:
    # Initialisation
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Input preparation
    firstname_input = 'firstname'
    lastname_input = 'lastname'
    email_input = 'email'
    file_input = 'file'

    file_name = "test.txt"
    with open(file_name, "w") as file:
        content = file.write("automationbypython")

    current_dir = path.abspath(path.dirname(__file__))  # get the path to the directory of the current executable file 
    file_path = path.join(current_dir, file_name)  # add the file name to this path 

    selectors_input = {
        firstname_input: "John",
        lastname_input: "Grey",
        email_input: "testmail@mail.test",
        file_input: file_path
        }

    # Input to required fields

    def send_keys_to_fields(selectors_input, selector_by):
        for selector, value in selectors_input.items():
            selector = browser.find_element(selector_by, selector)
            selector.send_keys(value)

    send_keys_to_fields(selectors_input, selector_by=By.NAME)

    # Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

    # Receive alert text

    def accept_alert_text(browser):
        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert text: {alert_text}")
        alert.accept()

    accept_alert_text(browser)

except Exception as e:
    print(e)

finally:
    browser.quit()

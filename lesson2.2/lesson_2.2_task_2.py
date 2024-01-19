from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from math import log, sin

try:
    # Initialisation
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Complete equation 
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    y = log(abs(12*sin(int(x))))
    print(f"{x} \n {y}")

    # Input to the field
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_field.send_keys(y)

    # Scroll down the page
    # # JS SCRIPT Scroll METHOD
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)

    # # Selenium scroll method
    input_field.location_once_scrolled_into_view

    # Activate required buttons

    robot_radiobutton = "#robotsRule"
    robot_checkbox = "#robotCheckbox"
    submit_button = "button.btn.btn-primary"

    button_selectors = [robot_checkbox, robot_radiobutton, submit_button]

    for selector in button_selectors:
        button = browser.find_element(By.CSS_SELECTOR, selector)
        button.click()

    # Receive alert text
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    alert.accept()

except Exception as e:
    print(e)

finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()

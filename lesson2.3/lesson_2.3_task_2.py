from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from math import log, sin

try:

    # Functions

    def click_button(selector, selector_by=By.CSS_SELECTOR):
        button = browser.find_element(selector_by, selector)
        button.click()         

    # Initialisation
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Confirmation modal
    submit_button = "button.btn.btn-primary"
    click_button(selector=submit_button)
    alert = browser.switch_to.alert
    alert.accept()

    # Complete equation 
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    equation = log(abs(12*sin(int(x))))

    # Input to the field and submit
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_field.send_keys(equation)
    click_button(selector=submit_button)

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

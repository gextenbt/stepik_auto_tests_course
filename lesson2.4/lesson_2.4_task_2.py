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
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Open and switch to other tab 
    book_button = "book"
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    click_button(selector=book_button, selector_by=By.ID)

    # Complete equation 
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    equation = log(abs(12*sin(int(x))))

    # Input to the field and submit
    submit_button = "solve"
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_field.send_keys(equation)
    click_button(selector=submit_button, selector_by=By.ID)

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

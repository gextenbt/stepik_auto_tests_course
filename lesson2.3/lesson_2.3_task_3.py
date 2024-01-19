from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from math import log, sin

try:

    # Functions

    def click_button(selector, selector_by=By.CSS_SELECTOR):
        button = browser.find_element(selector_by, selector)
        button.click()         

    # Initialisation
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Open and switch to other tab 
    trollface_button = "button.trollface.btn.btn-primary"
    click_button(selector=trollface_button)
    browser.switch_to.window(browser.window_handles[1])

    # Complete equation 
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    equation = log(abs(12*sin(int(x))))

    # Input to the field and submit
    submit_button = "button.btn.btn-primary"
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

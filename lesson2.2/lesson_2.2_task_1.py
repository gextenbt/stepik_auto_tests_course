from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значения x и y
    x = int(browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)").text)
    y = int(browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)").text)

    # Считаем сумму x и y
    eq = x + y
    print(x, y, eq)

    # Выбираем значение из выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(eq))

    # Нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем, пока не появится алерт
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())

    # Получаем текст алерта
    alert_text = alert.text
    print(f"Alert text: {alert_text}")

    # Принимаем алерт (нажимаем OK)
    alert.accept()

finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()

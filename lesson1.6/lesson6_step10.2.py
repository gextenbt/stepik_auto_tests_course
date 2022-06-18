from selenium import webdriver
import time
import random
import string
letters = string.ascii_lowercase

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
    for field in element1:
        field.send_keys(''.join(random.choice(letters) for _ in range(8)))
        
    element2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    for field in element2:
        field.send_keys(''.join(random.choice(letters) for _ in range(8))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


from selenium import webdriver
import time

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим "х" и вычисляем уравнение 
    x_element = browser.find_element_by_css_selector("span#input_value")
    x = x_element.text
    y = calc(x)
        
    # Ввести ответ в текстовое поле 
    field = browser.find_element_by_css_selector("input#answer")
    field.send_keys(y)

    # Отмечаем чекбоксы
    check= browser.find_element_by_css_selector("[for='robotCheckbox']")#"[]" - поиск по значению атрибута 
    check.click()
    #Отмечаем нужные radiobuttons
    radio= browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    # Нажимаем submit
    button= browser.find_element_by_css_selector("button.btn-default")
    button.click()
    
    
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

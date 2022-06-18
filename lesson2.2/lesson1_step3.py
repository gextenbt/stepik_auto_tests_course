
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    x=int(browser.find_element_by_css_selector("h2 span:nth-child(2)").text)
    y=int(browser.find_element_by_css_selector("h2 span:nth-child(4)").text)

    eq=x+y
    print(x, y, eq)
    
    snake = Select(browser.find_element_by_tag_name("select"))
    snake.select_by_value(str(eq))

    #Нажимаем submit
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

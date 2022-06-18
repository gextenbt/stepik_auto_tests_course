
from selenium import webdriver
import time



try:
    # Открываем ссылку
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # открываем линк stepik с ответом 
    linke = "https://stepik.org/lesson/165493/step/5?auth=registration&unit=140087"
    browser.get(linke)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

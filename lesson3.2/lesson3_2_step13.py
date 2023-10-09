from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# Watch source file lesson1.6_step11


class test_autofill(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):

        browser = self.driver
        browser.implicitly_wait(3)
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys("Volodymyr")
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Romaniv")
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys("test_email@gmail.com")

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст, и записываем в переменную
        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        # Возваращаем текст
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        # закрываем браузер после всех манипуляций
        self.driver.quit()

    "http://suninjuly.github.io/registration1.html"


if __name__ == "__main__":
    unittest.main()
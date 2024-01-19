from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestAutofill:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.teardown_method()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(3)
        browser.get(link)

        # Elements
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys("Volodymyr")
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Romaniv")
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys("test_email@gmail.com")

        # Send filled-in form
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        # Wait for page to load
        time.sleep(1)
        # Find the element containing text and store it in a variable
        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        # Return text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)
        assert registration_result == "Congratulations! You have successfully registered!"

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)
        assert registration_result == "Congratulations! You have successfully registered!"

    def teardown_method(self):
        # Close the browser after all manipulations
        self.driver.quit()

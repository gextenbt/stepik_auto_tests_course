from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
import math

@pytest.fixture(scope="session", autouse=True)
def hints_collection():
    collection = []
    yield collection
    print("\nHints Collection:")
    for hint in collection:
        print(hint)

class TestAutofill:
    TASK_LINKS = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]

    def create_time_answer(self):
        return math.log(int(time.time()))

    def fill_text_area(self, browser, link):
        browser.get(link) 
        wait = WebDriverWait(browser, 10)
        

        # Check if test was solved
        text_area = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'attempt textarea'))
        )
        
        again_button = browser.find_elements(
            By.CLASS_NAME, 'again-btn.white'
            )
        if again_button:
            again_button[0].click()


        # Fill in the form
        text_area = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'attempt textarea'))
        )
        text_area.send_keys(self.create_time_answer())

        # Send filled-in form
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )
        submit_button.click()

    @pytest.mark.parametrize("task_link", TASK_LINKS)
    def test_login(self, task_link, logged_in_browser, hints_collection):
        wait = WebDriverWait(logged_in_browser, 10)
        self.fill_text_area(logged_in_browser, link=task_link)
        
        hint_text = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'smart-hints.ember-view.lesson__hint')
                )
            ).text

        correct_hint_text = "Correct!"
        if hint_text != correct_hint_text:
            hints_collection.append(hint_text)
            print(hints_collection)
        assert hint_text == "Correct!", hint_text

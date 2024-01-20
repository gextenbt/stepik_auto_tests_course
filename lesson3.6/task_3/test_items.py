from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_elements(
        By.CSS_SELECTOR, "#add_to_basket_form > button"
        )
    # to test pytest -s -v --user_language=fr test_items.py
    # sleep(30)
    assert add_to_basket_button, "Add to basket button is missing"
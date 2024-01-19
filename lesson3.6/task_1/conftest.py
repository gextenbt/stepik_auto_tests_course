import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(scope="session", autouse=True)
def prepare_credentials():
    load_dotenv()
    credentials = {
        'email': os.getenv("EMAIL", default="default_email@example.com"),
        'password': os.getenv("PASSWORD", default="default_password")
        }
    return credentials

@pytest.fixture(scope="session")
def logged_in_browser(browser, prepare_credentials):
    credentials = prepare_credentials
    login_link = 'https://stepik.org/catalog?auth=login'
    browser.get(login_link)
    wait = WebDriverWait(browser, 10)
    
    # Wait for the login form to be present
    login_form = wait.until(EC.presence_of_element_located((By.ID, 'login_form')))

    # Elements
    login_form.find_element(
        By.ID, 'id_login_email'
        ).send_keys(credentials['email'])
    
    login_form.find_element(
        By.ID, 'id_login_password'
        ).send_keys(credentials['password'])

    # Send filled-in form
    login_form.find_element(By.CSS_SELECTOR, 'button').click()

    # Wait for the login form to become invisible
    wait.until(EC.invisibility_of_element_located((By.ID, 'login_form')))
    
    return browser
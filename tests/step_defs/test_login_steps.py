from _ast import Assert

import pytest_bdd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Scenarios

pytest_bdd.scenarios('../features/login.feature')


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters user name "{username}"'))
def login_user(browser, username):
    browser.maximize_window()
    user_name = browser.find_element(By.ID, 'userName')
    user_name.send_keys(username + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters password "{password}"'))
def login_pw(browser, password):
    pw = browser.find_element(By.ID, 'password')
    pw.send_keys(password + Keys.RETURN)


@pytest_bdd.when('the user clicks on login button')
def login_button(browser):
    browser.find_element(By.ID, 'login').click()


@pytest_bdd.then(pytest_bdd.parsers.parse('the user must get an error "{error_message}"'))
def error_phrase(browser, error_message):
    error = browser.find_element(By.ID, 'name').get_attribute('innerText')
    assert error == error_message
    browser.quit()



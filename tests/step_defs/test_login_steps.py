import pytest_bdd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

# Scenarios

pytest_bdd.scenarios('../features/login.feature')


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters user name "{username}"'))
def search_phrase(browser, username):
    browser.maximize_window()
    user_name = browser.find_element(By.ID, 'userName')
    user_name.send_keys(username + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('he user enters password "{password}"'))
def search_phrase(browser, password):
    browser.maximize_window()
    pw = browser.find_element(By.ID, 'password')
    pw.send_keys(password + Keys.RETURN)

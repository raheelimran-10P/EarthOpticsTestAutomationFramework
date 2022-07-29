"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

import pytest_bdd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# Scenarios

pytest_bdd.scenarios('../features/web.feature')


# When Steps

@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters first name "{fname}"'))
def firstname(browser, fname):
    browser.maximize_window()
    first_name = browser.find_element(By.ID, 'firstName')
    first_name.send_keys(fname + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters last name "{lname}"'))
def lastname(browser, lname):
    last_name = browser.find_element(By.ID, 'lastName')
    last_name.send_keys(lname + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters email "{email}"'))
def emailid(browser, email):
    email_id = browser.find_element(By.ID, 'userEmail')
    email_id.send_keys(email + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user selects the gender "{gender}"'))
def gender_iden(browser, gender):
    if gender == 'male':
        browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label').click()
    elif gender == 'female':
        browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[2]/label').click()
    elif gender == 'other':
        browser.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[3]/label').click()


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters phone number "{phone_number}"'))
def phone_no(browser, phone_number):
    ph_number = browser.find_element(By.ID, 'userNumber')
    ph_number.send_keys(phone_number + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user enters address "{user_address}"'))
def address_user(browser, user_address):
    address = browser.find_element(By.ID, 'currentAddress')
    address.send_keys(user_address + Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user select hobby "{user_hobby}"'))
def hobby(browser, user_hobby):
    if user_hobby == 'Sports':
        browser.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
    elif user_hobby == 'Reading':
        browser.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]').click()
    elif user_hobby == 'Music':
        browser.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()


@pytest_bdd.when(pytest_bdd.parsers.parse('the user selects subject "{subject}"'))
def subject(browser, subject):
    subjects = browser.find_element(By.ID, 'subjectsInput')
    subjects.send_keys(subject)
    browser.implicitly_wait(1)
    subjects.send_keys(Keys.RETURN)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user uploads picture "{picture_path}"'))
def profile_picture(browser, picture_path):
    picture = browser.find_element(By.ID, 'uploadPicture')
    picture.send_keys(picture_path)


@pytest_bdd.when(pytest_bdd.parsers.parse('the user selects dateofbirth "{dob}"'))
def dobs(browser, dob):
    dob_array = dob.split("-")
    browser.find_element(By.ID, 'dateOfBirthInput').click()
    month_select = Select(browser.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    month_select.select_by_visible_text(dob_array[1])
    year_select = Select(browser.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    year_select.select_by_visible_text(dob_array[2])
    browser.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[4]').click()


# then steps
@pytest_bdd.then('close the browser')
def close_browser(browser):
    browser.implicitly_wait(10)
    browser.quit()

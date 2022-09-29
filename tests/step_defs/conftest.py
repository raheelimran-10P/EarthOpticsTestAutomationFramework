import pytest
import requests

from pytest_bdd import given, parsers
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Constants

DemoQA_AutomationForm = 'https://demoqa.com/automation-practice-form'
DemoQA_AutomationForm2 = 'https://demoqa.com/login'
duck_duck_go = 'https://api.duckduckgo.com/'


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')



# Fixtures

@pytest.fixture
def browser():
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    #b = webdriver.Firefox();
    b = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    b.implicitly_wait(10)
    yield b


# Shared Given Steps

@given('the DemoQA home page is displayed')
def demoqa_autoform(browser):
    browser.get(DemoQA_AutomationForm)


@given('the DemoQA login page is displayed')
def demoqa_login(browser):
    browser.get(DemoQA_AutomationForm2)


@given(parsers.parse('the DuckDuckGo API is queried with "{phrase}"'), target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(duck_duck_go, params=params)
    return response


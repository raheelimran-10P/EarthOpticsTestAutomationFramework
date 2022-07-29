import requests

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
import json

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

# Scenarios

scenarios('../features/apitest.feature')


# Then Steps

@when(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code


@then(parsers.parse('the response contains results for "{phrase}"'))
def ddg_response_contents(ddg_response, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == ddg_response.json()['Heading'].lower()






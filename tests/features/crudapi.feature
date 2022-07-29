Feature: Test CRUD methods in Sample REST API Testing Framework
    As a user, I test CRUD methods
    to ensure POST, GET, UPDATE, DELETE HTTP methods are working as expected

Background:
    Given I set sample REST API URL
    And I set header param request content type as "application/json"


Scenario Outline: POST example
    Given I set "POST" posts api endpoint
    When  I send "POST" HTTP request with "<payload>"
    Then I receive valid HTTP response code "201" for "POST"
    And I expect response body "POST" is non-empty

    Examples:
      |   payload                                         |
      |   {"title": "foo", "body": "bar", "userId": 1}    |
      |   {"title": "bar", "body": "foo", "userId": 2}    |

Scenario: GET example
    Given I set "GET" posts api endpoint
    When I send "GET" HTTP request
    Then I receive valid HTTP response code "200" for "GET"
    And I expect response body "GET" is non-empty


Scenario Outline: DELETE example
    Given I set "DELETE" posts api endpoint for "1"
    When I send "DELETE" HTTP request with "<payload>"
    Then I receive valid HTTP response code "200" for "DELETE"
    And I expect response body "DELETE" is empty

    Examples:
       |   payload                                         |
       |   {"title": "foo", "body": "bar", "userId": 1}    |
       |   {"title": "abc", "body": "xyz", "userId": 1}    |



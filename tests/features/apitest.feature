Feature: DuckDuckGo Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API,
  So that my app can get answers anywhere.


  Background:
    Given the DuckDuckGo API is queried with "python"

  Scenario: Basic DuckDuckGo API Query
    When the response status code is "200"
    Then the response contains results for "python"













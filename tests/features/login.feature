Feature: Open DemoQA Web Browsing
  As an Automation Engineer,
  I want to fill invalid login details,
  So I can invalid credentials message.

  Background:
    Given the DemoQA login page is displayed

  Scenario: Enter login details
    When the user enters user name "Bisma"
    And the user enters password "bisma123"
    And the user clicks on login button
    Then the user must get an error "Invalid username or password!"
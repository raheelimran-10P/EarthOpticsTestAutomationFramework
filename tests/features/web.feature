Feature: Open DemoQA Login Page
  As an Automation Engineer,
  I want to fill student registration form,
  So I can learn pytest-bdd.

  Background:
    Given the DemoQA home page is displayed

  Scenario: Enter form details
    When the user enters first name "Bisma"
    And the user enters last name "Latif"
    And the user enters email "bismalatif@yopmail.com"
    And the user selects the gender "female"
    And the user enters phone number "11111111"
    And the user enters address "address--005street"
    And the user select hobby "Reading"
    And the user selects subject "maths"
    And the user uploads picture "C:\\Users\\bisma.latif\\Desktop\\12323.png"
    And the user selects dateofbirth "20-May-2002"
    Then close the browser









    

Feature: As a user I want to test the login functionality
         and much more
    Scenario: Login to the demo website
      Given the user is on login page
      When the user enters the credentials and logs in
      Then he should land on the correct page

    Scenario:Navigate to user profile page
       Given the user is on dashboard page
       When user clicks the user profile icon
       Then he should land on the correct profile page
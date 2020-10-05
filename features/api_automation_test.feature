Feature: To test API's using POST, GET, DELETE, PUT and PATCH operations

  Background:
	Given the user set sample REST API url

  @test1
  Scenario: Perform POST operation
    Given the user sets the POST api end point
    When the user set HEADER request content type as 'application/json'
    And the user sets the request body
    And the user sends the POST request
    Then the user gets the response status code as 201
    And the response text should not be empty

  @test2
  Scenario: Perform GET operation
    Given the user sets the GET api end point
    When the user set HEADER request content type as 'application/json'
    And the user sends the GET request
    Then the user gets the GET response status code  as 200

  @test3
  Scenario: Perform DELETE operation
    Given the user sets the DELETE api end point
    When the user set HEADER request content type as 'application/json'
    And the user sends the DELETE request
    Then the user gets the DELETE response status code  as 200

  @test4
  Scenario: Perform PUT operation
    Given the user sets the PUT api end point
    When the user set HEADER request content type as 'application/json'
    And the user sets the request body for PUT
    And the user sends the PUT request
    Then the user gets the PUT response status code  as 200

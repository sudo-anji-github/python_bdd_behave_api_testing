Feature: To test API's using POST, GET, DELETE, PUT and PATCH operations

  Background:
	Given the user set sample REST API url

  @test1
  Scenario: Perform POST operations
    Given the user sets the POST api end point
    When the user set HEADER request content type as 'application/json'
    And the user sets the request body
    And the user sends the POST request
    Then the user gets the response status code as 201

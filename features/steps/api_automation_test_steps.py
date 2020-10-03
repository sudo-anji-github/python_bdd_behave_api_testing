from behave import *
import requests

api_url = None
api_end_points = {}
request_headers = {}
request_body = {}
response_code = {}
response_text = {}

@given("the user set sample REST API url")
def rest_api_url(context):
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'


@given("the user sets the POST api end point")
def end_point(context):
    api_end_points['POST_URL'] = api_url+'/posts'


@when("the user set HEADER request content type as '{header_content}'")
def req_header(context, header_content):
    request_headers['Content-Type'] = header_content


@when("the user sets the request body")
def req_body(context):
    request_body['POST'] = {"title": "foo", "body": "bar", "userId": "1"}


@when("the user sends the POST request")
def send_post(context):
    response = requests.post(url=api_end_points['POST_URL'], json=request_body['POST'], headers=request_headers)
    response_code['POST_RESP_CODE'] = response.status_code
    response_text['POST_RESP_TEXT'] = response.text


@then("the user gets the response status code as {resp_code}")
def result_status(context, resp_code):
    assert response_code['POST_RESP_CODE'] is int(resp_code), "The response code is "+str(response_code['POST_RESP_CODE'])+". Should be "+resp_code

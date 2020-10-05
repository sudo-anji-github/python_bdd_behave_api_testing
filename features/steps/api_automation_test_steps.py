from behave import *
import requests
import pdb

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


#POST operation scenario

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


@then("the response text should not be empty")
def resp_text(context):
    assert len(response_text['POST_RESP_TEXT']) != 0, "The POST response text is "+response_text['POST_RESP_TEXT']+". Should not be empty"



#GET operation scenario

@given("the user sets the GET api end point")
def get_api_end_point(context):
    api_end_points['GET_URL'] = api_url + '/posts/1'


@when("the user sends the GET request")
def get_req(context):
    response = requests.get(url=api_end_points['GET_URL'], headers=request_headers)
    response_code['GET_RESP_CODE'] = response.status_code


@then("the user gets the GET response status code  as {status}")
def result(context, status):
    assert response_code['GET_RESP_CODE'] is int(status), "The response code is "+str(response_code['GET_RESP_CODE'])+". Should be "+status


#Delete operation scenario

@given("the user sets the DELETE api end point")
def del_api_end_point(context):
    api_end_points['DELETE_URL'] = api_url + '/posts/1'


@when("the user sends the DELETE request")
def del_req(context):
    response = requests.delete(url=api_end_points['DELETE_URL'], headers=request_headers)
    response_code['DEL_RESP_CODE'] = response.status_code
    response_text['DEL_RESP_TEXT'] = response.text


@then("the user gets the DELETE response status code  as {status}")
def del_resp(context, status):
    assert response_code['DEL_RESP_CODE'] is int(status), "The response code is "+str(response_code['DEL_RESP_CODE'])+". Should be "+status


#PUT operation scenario

@given("the user sets the PUT api end point")
def put_api_end_point(context):
    api_end_points['PUT_URL'] = api_url + '/posts/1'


@when("the user sets the request body for PUT")
def req_body(context):
    request_body['PUT'] = {"title": "python", "body": "QA automation", "userId": "1437"}


@when("the user sends the PUT request")
def send_post(context):
    response = requests.put(url=api_end_points['PUT_URL'], json=request_body['PUT'], headers=request_headers)
    response_code['PUT_RESP_CODE'] = response.status_code
    response_text['PUT_RESP_TEXT'] = response.text


@then("the user gets the PUT response status code  as {status}")
def put_resp(context, status):
    assert response_code['PUT_RESP_CODE'] is int(status), "The response code is " + str(response_code['PUT_RESP_CODE']) + ". Should be " + status
import ast
import pytest
import requests
from pytest_bdd import given, when, then, parsers, scenarios
import json

scenarios('../features/crudapi.feature')


@given('I set sample REST API URL')
def set_rest_api_url():
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'


@given(parsers.parse('I set header param request content type as "{header_content_type}"'))
def set_header_without_request_body(header_content_type):
    global content_type
    content_type = header_content_type


@given(parsers.parse('I set "{request_type}" posts api endpoint'))
def set_post_and_get_api_endpoint(request_type):
    if request_type == "POST":
        global post_api_endpoint
        post_api_endpoint = api_url + '/posts'
        print('POST ENDPOINT URL: {}'.format([post_api_endpoint]))

    elif request_type == 'GET':
        global get_api_endpoint
        get_api_endpoint = api_url + '/posts/'
        print('GET ENDPOINT URL: {}'.format([get_api_endpoint]))



@given(parsers.parse('I set "{request_type}" posts api endpoint for "{id}"'))
def set_put_and_delete_api_endpoint(request_type, id):
    if request_type == "PUT":
        global put_api_endpoint
        put_api_endpoint = api_url + '/posts/' + id
        print('PUT ENDPOINT URL: {}'.format([put_api_endpoint]))
    elif request_type == "DELETE":
        global delete_api_endpoint
        delete_api_endpoint = api_url + '/posts/' + id
        print('DELETE ENDPOINT URL: {}'.format([delete_api_endpoint]))


@when(parsers.parse('I send "{request_type}" HTTP request with "{payload}"'))
def send_post_request(request_type, payload):
    if request_type == "POST":
        response = requests.post(url=post_api_endpoint,
                                 data=json.dumps(ast.literal_eval(payload)),
                                 headers={"content-type": 'Content-Type', "charset": "UTF-8"})
        global post_response
        post_response = response.json()
        print(post_response)
        print("post_response: {}".format([post_response]))


        global post_status_code
        post_status_code = response.status_code
        print(response.status_code)

    if request_type == "PUT":
        response = requests.put(url=put_api_endpoint,
                                data=json.dumps(ast.literal_eval(payload)),
                                headers={"content-type": 'Content-Type', "charset": "UTF-8"})
        global put_response
        put_response = response.json()
        print("put_response: {}".format([put_response]))
        global put_status_code
        put_status_code = response.status_code
    elif request_type == "DELETE":
        response = requests.delete(url=delete_api_endpoint,
                                   data=payload,
                                   headers={"content-type": 'Content-Type', "charset": "UTF-8"})
        global delete_response
        delete_response = response.json()
        print("delete_response: {}".format([delete_response]))
        global delete_status_code
        delete_status_code = response.status_code


@when(parsers.parse('I send "{request_type}" HTTP request'))
def send_get_request(request_type):
    if request_type == "GET":
        response = requests.get(url=get_api_endpoint,
                                headers={"content-type": 'Content-Type', "charset": "UTF-8"})
        global get_response
        get_response = response.json()
        print("get_response: {}".format([get_response]))
        global get_status_code
        get_status_code = response.status_code


@then(parsers.parse('I receive valid HTTP response code "{status_code}" for "{request_type}"'))
def validate_request(status_code, request_type):
    if request_type == "POST":
        print([post_status_code])
        assert post_status_code == int(status_code)
    elif request_type == "GET":
        print([get_status_code])
        assert get_status_code == int(status_code)
    elif request_type == "PUT":
        print([put_status_code])
        assert put_status_code == int(status_code)
    elif request_type == "DELETE":
        print([delete_status_code])
        assert delete_status_code == int(status_code)


@then(parsers.parse('I expect response body "{request_type}" is non-empty'))
def validate_response_body(request_type):
    if request_type == "POST":
        assert post_response is not None
    elif request_type == "GET":
        assert get_response is not None
    elif request_type == "PUT":
        assert put_response is not None
    elif request_type == "DELETE":
        assert delete_response == {}


@then(parsers.parse('I expect response body "{request_type}" is empty'))
def validate_delete_response_body(request_type):
    assert delete_response == {}

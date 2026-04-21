from common.request import request_api

def test_api():
    resp =request_api("post","https://reqres.in/api/users?page=2")

    assert resp.status_code ==401


import requests
#参数接口请求
def request_api(method,url,data=None,params=None,json=None):

    resp = requests.request(
        url = url,
        method=method,
        data=data,
        params=params,
        json=json
    )

    return resp



# import requests
# def get(url):
#     res=requests.get(url)
#     assert res.status_code ==200
#     return res
# def post_json(url,body):
#     res=requests.post(url,json=body)
#     assert res.status_code==201
#     return res

import requests
def get(url):
    res=requests.get(url)
    assert res.status_code ==200
    return res
def post_json(url,body):
    res=requests.post(url,json=body)
    assert res.status_code==201
    return res
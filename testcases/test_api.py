# import allure
# from config.settings import get_config
# config =get_config("dev")
# BASE_URL =config["base_url"]
# from utils.request_util import get,post_json
# @allure.title("获取信息")
# def test_get_user():
#     url =f"{BASE_URL}/users/1"
#     with allure.step("发送请求"):
#         res = get(url)
#     with allure.step("断言id是1"):
#         assert res.json()["id"]==1
# @allure.title("获取帖子列表")
# def test_post():
#     url =f"{BASE_URL}/posts"
#     res =get(url)
#     assert isinstance(res.json(),list)
#     assert len(res.json())>0
# @allure.title("创建帖子")
# def test_create_post():
#     url =f"{BASE_URL}/posts"
#     body ={"title":"test"}
#     res =post_json(url,body)
#     assert res.json()["title"]=="test"
#
# from config.settings import get_config
# from utils.request_util import get
# config=get_config("dev")
# BASE_URL=config["base_url"]
# def test_get_user():
#     url=f"{BASE_URL}/users/1"
#     res=get(url)
#     assert res.json()["id"]==1


# from config.settings import get_config
# from utils.request_util import get
# config =get_config("dev")
# BASE_URL=config["base_url"]
# def test_get_user():
#     url=f"{BASE_URL}/users/1"
#     res=get(url)
#     assert res.json()[id]==1

import allure
from config.settings import get_config
from utils.request_util import get,post_json
config=get_config("dev")
BASE_URL=config.get("base_url")
@allure.title("获取信息")
def test_get_user():
    url=f"{BASE_URL}/users/1"
    with allure.step("发送请求"):
        res=get(url)
    with allure.step("断言id是1"):
        assert res.json()["id"]==1
@allure.title("获取帖子列表")
def test_posts():
    url=f"{BASE_URL}/posts"
    res=get(url)
    assert isinstance(res.json(),list)
    assert len(res.json())>0
@allure.title("创建帖子")
def test_create_post():
    url=f"{BASE_URL}/posts"
    body={"title":"test"}
    res=post_json(url,body)
    assert res.json()["title"]=="test"
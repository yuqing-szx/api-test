import allure
from common.load_yaml import load_yaml
from common.request import request_api
import pytest



data = load_yaml("data/reqres_data.yaml")
@pytest.mark.parametrize("yaml",data)
@allure.epic("接口测试")
@allure.feature("数据驱动测试")
@allure.story("yaml读取-请求-断言")
def test_yaml(yaml):

    resp = request_api(yaml["method"], yaml["url"])

    assert resp.status_code== yaml["expected"]["status_code"]

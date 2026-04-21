import allure
import pytest


@allure.epic("allure项目")
@allure.feature("判断集合")
@allure.story("数字")
@allure.title("预期错误")
def test_1():
    assert 1==2

@allure.epic("allure项目")
@allure.feature("判断集合")
@allure.story("数字")
@allure.title("预期正确")
def test_2():
    assert 1==1

@allure.epic("allure项目")
@allure.feature("判断集合")
@allure.story("字符串")
@allure.title("预期正确")
def test_3():
    assert "abc" == "abc"
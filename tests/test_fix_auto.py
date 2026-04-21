#这是单独练习fixture全局使用与独立使用方式的测试文件
from datetime import datetime

import pytest

# True：所有用例全部使用fix函数
# function:用例独立使用函数，session：所有用例共享fix函数
@pytest.fixture(autouse=True,scope="function")
def fix():
    print(datetime.now(),"开始执行用例")
    yield
    print(datetime.now(),"用例执行完毕")



def test1(fix):
    pass

@pytest.mark.usefixtures("fix")
def test2():
    pass
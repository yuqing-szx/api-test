#fixture配置文件，函数在这可被所有测试用例调用
from datetime import datetime

import pytest


@pytest.fixture(autouse=True,scope="session")
def fix():
    print(datetime.now(),"开始执行用例")
    yield
    print(datetime.now(),"用例执行完毕")



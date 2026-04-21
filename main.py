#框架启动入口
import pytest
import os


pytest.main()

os.system("allure generate -o report -c temps")


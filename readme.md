# Python + Pytest 接口自动化测试框架

## 项目简介

这是一个基于 Python 的接口自动化测试框架，用于对  API 进行自动化测试。框架实现了数据驱动、请求封装、断言验证和可视化报告等功能。

## 技术栈
- Python + Pytest（测试框架）
- Requests（HTTP 请求封装）
- PyYAML（数据驱动）
- Allure（测试报告）
- Git（版本管理）


## 项目结构

pytest_demo1/
├── common/ # 公共模块
│ ├── load_yaml.py # YAML 文件读取
│ ├── request.py # Requests 请求封装
│ └── extract.py # 响应结果提取
├── data/ # 测试数据
│ └── reqres_data.yaml # YAML 格式的测试用例
├── tests/ # 测试用例
│ ├── test_api.py # 接口测试用例
│ ├── test_yaml.py # 数据驱动测试用例
│ ├── test_allure.py # Allure 报告示例
│ └── test_web.py # Web UI 测试（需配置 selenium）
├── report/ # Allure 报告输出目录
├── temps/ # 测试过程临时数据
├── conftest.py # pytest 全局夹具
├── pytest.ini # pytest 配置文件
├── main.py # 框架启动入口
└── README.md # 项目说明









import allure
import pytest


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录成功的用例1")

    @allure.story("登录成功")
    def test_login_success2(self):
        print("这是登录成功的用例2")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录失败的用例")

    @allure.story("登录失败")
    def test_login_fail2(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        with allure.step("点击登录"):
            print("进行登录")
        with allure.step("断言"):
            assert "1" == 1
            print("登录失败")

# # 生成测试结果
# pytest test_sample.py --alluredir=./allure-results
#
# # 运行指定feature/story的测试用例
# pytest test_sample.py --allure_features "登录模块" --allure-stories "登录成功"
#
# # 直接使用默认浏览器打开测试报告
# allure serve ./allure-results
# # 或者生成测试报告，再打开测试报告
# allure generate ./allure-results -o ./allure-report --clean
# allure open -h 127.0.0.1 -p 8083 ./allure-report


#
# @pytest.fixture()
#
# def func(x):
#     print("func")
#     return x + 1
#
# @allure.title("test_func1")
# def test_func1():
#     assert func(4) == 5  # 成功示例
#     print("test1")
#
# @allure.title("test_func2")
# def test_func2():
#     assert func(3) == 5  # 失败示例
#     print("test1")
#
# if __name__ == '__main__':
#     pytest.main(['test_sample.py'])
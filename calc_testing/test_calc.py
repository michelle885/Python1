"""
编写 Calc 这个类add() ，div() 这两个方法的测试用例
按照等价类去设计测试用例
把代码上传到github, 并回贴你的github的地址
"""
# 引入pytest, yaml, Calc类
import pytest
import yaml
from demo.calc_testing.calc import Calc


# 定义一个setup module函数，在执行Python文件之前被调用
def setup_module():
    print("setup module")

# 定义一个teardown module函数，在执行Python文件之后被调用
def teardown_module():
    print("teardown module")

# 定义一个TesCalc类，用于测试Calc类
class TestCalc:
    # 定义一个setup class方法，在执行TestCalc类之前被调用
    def setup_class(self):
        print("setup class")
        # 声明Calc的实例
        self.calc = Calc()
        # self.data = yaml.safe_load(open("data.yml"))
        # self.add_data1 = self.data["add"]
        # self.div_data1 = self.data["div"]

    # 定义一个teardown class方法，在执行TestCalc类之后被调用
    def teardown_class(self):
        print("teardown class")

    # 定义一个setup方法，在执行测试用例之前被调用
    def setup(self):
        print("setup")

    # 定义一个setup方法，在执行测试用例之后被调用
    def teardown(self):
        print("teardown")

    # 定义一个data变量，将data.yml里面的数据读出来
    data = yaml.safe_load(open("data.yml", encoding='UTF-8'))
    # data为一个字典，用key值取出对应的列表赋值给add_data1和div_data1
    add_data1 = data["add"]
    div_data1 = data["div"]

    # 用 add_data1 给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', add_data1)
    # 定义一个test_add方法用于测试 Calc里面的add方法
    def test_add(self, a, b, expect):
        # 将 a和b 传入Calc里面的add方法，将结果赋值给result
        result = self.calc.add(a,b)
        # 用 assert 断言，比对 result和expect的值是否相等
        assert result == expect
        print("result is {}, expect is {}".format(result,expect))

    # 用 div_data1 给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', div_data1)
    # 定义一个test_div方法用于测试 Calc里面的div方法
    def test_div(self, a, b, expect):
        # 将 a和b 传入Calc里面的div方法，将结果赋值给result
        result = self.calc.div(a,b)
        # 用 assert 断言，比对 result和expect的值是否相等
        assert result == expect
        print("result is {}, expect is {}".format(result, expect))

# python解释器的入口函数
if __name__ == '__main__':
    # 用pytest的main函数，执行所有符合pytest条件（文件名为test_开头，类名为Test开头，方法名为test_开头）的测试用例
    pytest.main()

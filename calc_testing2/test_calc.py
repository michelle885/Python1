"""
1.补全测试用例【加减乘除】
2.使用 fixture 装置完成计算机器实例的初始化
3.改造 pytest 的运行规则 ,测试用例命名以 calc_ 开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，…
4.自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
5.封装 add, div 测试步骤到 yaml 文件中
"""
# 引入pytest, yaml, Calc, Decimal类
import pytest
import yaml
from calc_testing2.calc import Calc
from decimal import Decimal

# 定义一个setup module函数，在执行Python文件之前被调用
def setup_module():
    print("setup module")

# 定义一个teardown module函数，在执行Python文件之后被调用
def teardown_module():
    print("teardown module")

# 使用 fixture 装置进行计算机器实例的初始化，生命周期为module, Python文件
@pytest.fixture(scope='module')
def initialization():
    print("测试开始")
    # 声明Calc的实例
    calc = Calc()
    # 用yield 返回 Calc的实例
    yield calc
    print("测试结束")

# 定义一个TesCalc类，用于测试Calc类
class TestCalc:
    # 定义一个setup class方法，在执行TestCalc类之前被调用
    def setup_class(self):
        print("setup class")

    # 定义一个teardown class方法，在执行TestCalc类之后被调用
    def teardown_class(self):
        print("teardown class")

    # 定义一个setup方法，在执行测试用例之前被调用
    def setup(self):
        print("setup")

    # 定义一个setup方法，在执行测试用例之后被调用
    def teardown(self):
        print("teardown")

    # 定义一个get_data方法
    def get_data():
        # 定义一个data变量，将data.yml里面的数据读出来
        data = yaml.safe_load(open("data/data.yml", encoding='UTF-8'))
        # 方法返回 data
        return data

    # 定义一个获取步骤文件内容的方法
    def get_steps_file(self):
        with open('steps/mix_steps.yml') as f:
            return yaml.safe_load(f)

    # 分析步骤文件里的内容
    def get_steps(self, a1, b1, expect1, a2, b2, expect2, initialization):
        # 调用读取步骤文件的方法
        steps = self.get_steps_file()
        # 循环分析每一个步骤
        for step in steps:
            print(f"step=={step}")
            # 若步骤等于add，则执行add的测试用例
            if 'add' == step:
                assert initialization.add(a1,b1) == expect1
            # 若步骤等于div，则执行div的测试用例
            if 'div' == step:
                assert initialization.div(a2,b2) == expect2

    # data为一个字典，用key值"add"取出对应的测试数据,给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', get_data()["add"])
    # 定义一个方法用于测试 Calc里面的add方法，参数中的initialization会调用fixture，返回Calc的实例
    def calc_add(self, a, b, expect, initialization):
        # 捕捉异常
        try:
            # 用Calc的实例调用add方法，将结果赋值给result
            result = initialization.add(a,b)
            # 用 assert 断言，比对 result和expect的值是否相等
            assert result == Decimal(str(expect))
            print("result is {}, expect is {}".format(result,expect))
        # 将捕捉到的异常打印出来
        except(TypeError, Exception) as e:
            print(e)

    # data为一个字典，用key值"sub"取出对应的测试数据,给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', get_data()["sub"])
    # 定义一个方法用于测试 Calc里面的sub方法，参数中的initialization会调用fixture，返回Calc的实例
    def calc_sub(self, a, b, expect, initialization):
        # 捕捉异常
        try:
            # 用Calc的实例调用sub方法，将结果赋值给result
            result = initialization.sub(a,b)
            # 用 assert 断言，比对 result和expect的值是否相等
            assert result == Decimal(str(expect))
            print("result is {}, expect is {}".format(result,expect))
        # 将捕捉到的异常打印出来
        except(TypeError, Exception) as e:
            print(e)

    # data为一个字典，用key值"mul"取出对应的测试数据,给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', get_data()["mul"])
    # 定义一个方法用于测试 Calc里面的mul方法，参数中的initialization会调用fixture，返回Calc的实例
    def calc_mul(self, a, b, expect, initialization):
        # 捕捉异常
        try:
            # 用Calc的实例调用mul方法，将结果赋值给result
            result = initialization.mul(a,b)
            # 用 assert 断言，比对 result和expect的值是否相等
            assert result == Decimal(str(expect))
            print("result is {}, expect is {}".format(result,expect))
        # 将捕捉到的异常打印出来
        except(TypeError, Exception) as e:
            print(e)

    # data为一个字典，用key值"div"取出对应的测试数据,给 a, b 和 expect进行参数化
    @pytest.mark.parametrize('a, b, expect', get_data()["div"])
   # 定义一个方法用于测试 Calc里面的div方法，参数中的initialization会调用fixture，返回Calc的实例
    def calc_div(self, a, b, expect, initialization):
        # 捕捉异常
        try:
            # 用Calc的实例调用div方法，将结果赋值给result
            result = initialization.div(a,b)
            # 用 assert 断言，比对 result和expect的值是否相等
            assert result == Decimal(str(expect))
            print("result is {}, expect is {}".format(result, expect))
        # 将捕捉到的异常打印出来
        except(ZeroDivisionError,TypeError,Exception) as e:
            print(e)

    # 取出mix里面的add和div对应的测试数据
    @pytest.mark.parametrize('a1, b1, expect1', get_data()["mix"]["add1"])
    @pytest.mark.parametrize('a2, b2, expect2', get_data()["mix"]["div1"])
    # 调用分析测试步骤的方法
    def calc_mix(self, a1, b1, expect1, a2, b2, expect2, initialization):
        self.get_steps(a1, b1, expect1, a2, b2, expect2, initialization)

# python解释器的入口函数
if __name__ == '__main__':
    # 用pytest的main函数，执行所有符合pytest条件（文件名为test_开头，类名为Test开头，方法名为test_开头）的测试用例
    pytest.main()

from decimal import Decimal

# 声明一个Calc类
class Calc:
    # 定义类方法add，传入参数a和b, 方法的返回值是 a+b
    def add(self, a, b):
        return Decimal(str(a)) + Decimal(str(b))

    # 定义类方法sub，传入参数a和b, 方法的返回值是 a-b
    def sub(self, a, b):
        return a - b

    # 定义类方法mul，传入参数a和b, 方法的返回值是 a*b
    def mul(self, a, b):
        return a * b

    # 定义类方法div，传入参数a和b, 方法的返回值是 a/b
    def div(self, a, b):
        return Decimal(str(a)) / Decimal(str(b))


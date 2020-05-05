"""
手机
"""
print("-----------------Phone 类1-----------------")
# 声明一个Phone类
class Phone:
    # 类变量，静态变量
    brand = "HUAWEI"
    price = 4000
    color = "white"

    # 类中的函数，方法
    def charge(self):
        print("我在充电~~")
    def call(self):
        print("我在打电话~~")

## 直接调用类属性
print(Phone.brand)
print(Phone.price)
## 类的实例化
phone = Phone()
## 调用实例对象中的属性
print(phone.color)
## 调用实例对象中的方法
phone.charge()
phone.call()


"""
宝宝
"""
print("-----------------Baby 类2-----------------")
# 声明一个baby类
class Baby:
    # 类变量，静态变量
    height = 80
    # 私有变量
    __weight = 25
    # 类中的函数，方法
    def eat(self):
        print("宝宝在吃饭~~")
    def play(self):
        # 私有属性可以在类的方法里调用，前面加上 self.
        print("私有变量是",self.__weight)
        print("宝宝在玩~~")
    # 私有属性，私有方法
    def __cry(self):
        print("宝宝哭了~~")

## 类的实例化
xiaofang = Baby()
## 调用实例对象中的属性
print(xiaofang.height)
## 名字重写，用_加类名可以调用到私有属性
print(xiaofang._Baby__weight)
## 调用实例对象中的方法
xiaofang.eat()
xiaofang.play()
## 名字重写，用_加类名可以调用到私有方法
xiaofang._Baby__cry()


"""
汽车
"""
print("-----------------Car 类3-----------------")
# 声明一个Car类
class Car:
    # 类变量，静态变量
    wheel = 4
    # 类方法，需要传入一个km参数
    def run(self,km):
        print("汽车的里程数是{}公里".format(km))

## 类的实例化
qiche = Car()
## 调用实例对象的属性
print(qiche.wheel)
## 调用实例对象的方法，并传参
qiche.run(0)

"""
电动汽车
"""
print("-----------------ElectricCar 类4-----------------")
# 声明一个ElectricCar类，继承Car类
class ElectricCar(Car):
    def license(self):
        print("电动汽车可免费领取汽车牌照")
## 声明一个电动汽车的实例
elec = ElectricCar()
## 子类调用父类的属性
print(elec.wheel)
## 子类调用父类的方法，并传参
elec.run(50)
## 子类调用自己类的方法
elec.license()

"""
油电混合汽车
"""
print("-----------------MixCar 类5-----------------")
# 声明一个MixCar类，继承Car类
class MixCar(Car):
    # 初始化，构造函数
    def __init__(self,p):
        # 实例变量
        self.price = p
    # 定义一个公有方法，调用私有属性，参数加上 self.
    def get_price(self):
        print("油电混合汽车价格为",self.price)
## 在类的初始化时，给init定义的参数传参
mix = MixCar(100000)
print(mix.wheel)
mix.run(80)
mix.get_price()
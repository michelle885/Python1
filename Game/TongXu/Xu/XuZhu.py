"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
# 从demo.Game.TongXu.Tong文件夹里面的TongLao文件里，引入TongLao类
from demo.Game.TongXu.Tong.TongLao import TongLao
# 声明XuZhu类，继承TongLao
class XuZhu(TongLao):
    # 定义一个read（念经）的方法，打印“罪过罪过”
    def read(self):
        print("罪过罪过")
    # 重构父类（童姥类）的方法see_people, 传入姓名参数
    def see_people(self, name):
        # 利用format函数将参数name打印出来
        print("{}，善哉善哉".format(name))
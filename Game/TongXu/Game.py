"""
游戏运行入口
"""
# 从demo.Game.TongXu.Tong文件夹里面的TongLao文件里，引入TongLao类
from demo.Game.TongXu.Tong.TongLao import TongLao
# 从demo.Game.TongXu.Xu文件夹里面的XuZhu文件里，引入XuZhu类
from demo.Game.TongXu.Xu.XuZhu import XuZhu

# 打印童姥出场分割线
print("-----------------童姥出场-----------------")
# 声明童姥实例，并初始化童姥的初始血量和武力值
tonglao = TongLao(1000,200)
# 用童姥实例调用童姥类的see_people方法，并传入name参数 WYZ
tonglao.see_people('WYZ')
# 用童姥实例调用童姥类的see_people方法，并传入name参数 李秋水
tonglao.see_people('李秋水')
# 用童姥实例调用童姥类的see_people方法，并传入name参数 丁春秋
tonglao.see_people('丁春秋')
# 用童姥实例调用童姥类的see_people方法，并传入name参数 段誉
tonglao.see_people('段誉')
# 用童姥实例调用童姥类的fight_zms方法，并传入敌人的初始血量和武力值参数 enemy_hp和enemy_power
tonglao.fight_zms(1000,50)

# 打印虚竹出场分割线
print("-----------------虚竹出场-----------------")
# 声明虚竹实例，并调用它的父类（童姥类）的init方法，初始化虚竹的初始血量和武力值
xuzhu = XuZhu(1000,100)
# 用虚竹实例调用虚竹类中被重构的see_people方法，并传入name参数 段誉
xuzhu.see_people('段誉')
# 用虚竹实例调用虚竹类的read方法
xuzhu.read()




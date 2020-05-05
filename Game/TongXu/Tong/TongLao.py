"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
1.see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2.fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
"""
# 声明TongLao类
class TongLao:
    # 初始化，给血量和武力值赋值，若不传参，则hp为默认值1000，power为默认值100
    def __init__(self, hp=1000 , power=100):
        # self调用类的属性，用init传进来的参数初始化
        self.hp = hp
        self.power = power
        # 将初始血量和武力值打印出来
        print("初始血量为", hp, "，武力值为", power)
    # 定义see_people方法， 传入姓名参数
    def see_people(self, name):
        # 如果name等于 XYZ, 则打印 “师弟！！！！”
        if name=='WYZ':
            print("师弟！！！！")
        # 如果name等于 李秋水, 则打印 “呸，贱人”
        if name=='李秋水':
            print("呸，贱人")
        # 如果name等于 丁春秋, 则打印 “叛徒！我杀了你”
        if name=='丁春秋':
            print("叛徒！我杀了你")
        # 如果name不等于以上值，则打印 "幸会幸会~"
        else:
            print("幸会幸会~")

    # 定义fight_zms方法， 传入敌人的 hp和 power
    def fight_zms(self, enemy_hp, enemy_power):
        # self调用TongLao类的属性 hp，使其武力值提升10倍
        self.hp = self.hp * 10
        # self调用TongLao类的属性 power，使其血量缩减2倍
        self.power = self.power / 2
        # 用TongLao的血量减去敌人的武力值，计算TongLao最终的血量
        final_hp = self.hp - enemy_power
        # 用敌人的血量减去TongLao的武力值，计算敌人最终的血量
        final_enemy_hp = enemy_hp - self.power
        # 若TongLao的最终血量大于敌人最终血量，则打印童姥获胜
        if final_hp > final_enemy_hp:
            print("童姥获胜！")
        # 若TongLao的最终血量小于敌人最终血量，则打印敌人获胜
        elif final_hp < final_enemy_hp:
            print("敌人获胜！")
        # 若TongLao的最终血量等于敌人最终血量，则打印平局
        else:
            print("平局~")


"""
游戏规则：
设定一个回合制2人对打游戏。
每个人物都有hp，power，skill
hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
"""
# 引入yaml类
import yaml
# 声明GameYaml类
class GameYaml():
    # 定义构造方法，初始化，带有self.的变量是为了后面的方法可以访问
    def __init__(self):
        # 用yaml的safe_load函数读取yaml文件，将转换的python对象赋值给data
        data = yaml.safe_load(open("./game.yaml"))
        # print(data)
        # data的python对象是 {'Tonglao': {'hp': 1000, 'power': 200, 'skill': 2},
        # 'Liqiushui': {'hp': 1500, 'power': 80, 'skill': 2},
        # 'Dingchunqiu': {'hp': 1200, 'power': 70, 'skill': 2},
        # 'default': ['Tonglao', 'Liqiushui']}

        # 在data中，将key值为“default”的value赋值给default
        default = data["default"]
        # default为一个列表['Tonglao', 'Liqiushui']
        # 取列表里的第0个值的选手姓名，赋值给first_man
        self.first_man = default[0]
        # 取列表里的第1个值的选手姓名，赋值给second_man
        self.second_man = default[1]
        # 在data中，key值为self.first_man的value是{'hp': 1000, 'power': 200, 'skill': 2}
        # 分别通过key值为"hp"，"power"和"power"取出对应的value，赋值给first_man的hp, power 和 skill
        self.first_man_hp = data[self.first_man]["hp"]
        self.first_man_power = data[self.first_man]["power"]
        self.first_man_skill = data[self.first_man]["skill"]
        # 在data中，key值为self.second_man的value是{'hp': 1500, 'power': 80, 'skill': 2}
        # 分别通过key值为"hp"，"power"和"power"取出对应的value，赋值给second_man的hp, power 和 skill
        self.second_man_hp = data[self.second_man]["hp"]
        self.second_man_power = data[self.second_man]["power"]
        self.second_man_skill = data[self.second_man]["skill"]

    # 定义一个fight方法
    def fight(self):
        # 定义一个记录比赛次数的变量，初始值为0
        round = 0
        print("-----------比赛开始-----------")
        # 用format函数将比赛的两个选手姓名打印出来
        print("比赛的选手分别是{}和{}".format(self.first_man,self.second_man))
        # 定义一个True循环，它是一个死循环，直到break跳出循环为止
        while True:
            # 每次比赛会增加1
            round += 1
            # 用format函数将比赛的次数打印出来
            print("-----------第{}轮比赛-----------".format(round))
            # 用取余函数，比赛次数是3的倍数，则执行
            if (round%3 == 0):
                # 用选手1的血量减去 选手2的武力值 乘以 选手2的技能值，计算选手1最终的血量
                self.first_man_hp = self.first_man_hp - self.second_man_power*self.second_man_skill
                # 用选手2的血量减去 选手1的武力值 乘以 选手1的技能值，计算选手2最终的血量
                self.second_man_hp = self.second_man_hp - self.first_man_power*self.first_man_skill
            # 比赛次数不是3的倍数，则执行
            else:
                # 用选手1的血量减去 选手2的武力值，计算选手1最终的血量
                self.first_man_hp = self.first_man_hp - self.second_man_power
                # 用选手2的血量减去 选手1的武力值，计算选手2最终的血量
                self.second_man_hp = self.second_man_hp - self.first_man_power
            # 用format函数将两个选手的姓名和实时血量打印出来
            print("{}’s hp is {}".format(self.first_man, self.first_man_hp))
            print("{}’s hp is {}".format(self.second_man, self.second_man_hp))
            # 如果选手1血量小于等于0，则打印选手1输，并退出循环
            if self.first_man_hp <= 0:
                print("{} is loser".format(self.first_man))
                break
            # 如果选手2血量小于等于0，则打印选手2输，并退出循环
            elif self.second_man_hp <= 0:
                print("{} is loser".format(self.second_man))
                break

# 如果__name__等于'__main__', 也就是说只有当前模块才能执行到
if __name__ == '__main__':
    # 声明一个GameYaml类的实例
    game = GameYaml()
    # 用实例game调用GameYaml类的fight方法
    game.fight()


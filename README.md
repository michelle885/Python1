作业0 -- Bubble.py
冒泡排序每一行加注释说明

作业1 -- MyClass.py
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

作业2 -- TongXu 文件夹
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
希望各位同学在此基础上可以添加自己的“freestyle”哦

作业3 -- List.py
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
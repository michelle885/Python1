"""
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
"""
# 声明List类
class List():
    # 定义一个square1方法，传入参数 a，类型提示是list
    def square1(self,a:list):
        # 用列表推导式，计算每个数的平方值并存到类的属性 a
        self.a = [i**2 for i in a]
        # 利用列表里的sort()函数进行排序
        self.a.sort()
        # 打印输出取完平方值并排序号的类的属性a
        print(self.a)

    # 定义一个square2方法，传入参数 a，类型提示是list
    def square2(self,a:list):
        # 用列表推导式，先计算每个数的平方值，再用sorted()函数进行排序，并存到类的属性 a
        self.a = sorted([i**2 for i in a])
        # 打印输出取完平方值并排序号的类的属性a
        print(self.a)
# 定义2个列表变量
list1 = [-4,-1,0,3,10]
list2 = [-7,-3,2,3,11]
# 声明一个List类的实例
a = List()
# 打印方法一的分割线
print("-----------------方法一-----------------")
# 用List实例调用square1方法
a.square1(list1)
a.square1(list2)

# 打印方法二的分割线
print("-----------------方法二-----------------")
# 用List实例调用square2方法
a.square2(list1)
a.square2(list2)



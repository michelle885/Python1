"""
冒泡排序
"""
class Bubble: #声明一个Bubble类
    def bubble_sort(self,list): #声明一个bubble_sort()函数
        n = len(list) #计算列表长度
        for i in range(n-1): #循环的排序次数， range(n-1)表示 0，1...n-2，共 n-1 次循环
            for j in range(i+1,n): #每次比对的次数， range(i+1，n) 其中i+1表示每次都是和i后面的数开始比对，一直比到最后一个数 list[n-1]
                if list[i] > list[j]: #如果前面的数比后面的数大
                    list[i],list[j] = list[j],list[i]  #将 list[i] 和 list[j] 交换
        print(list1) #打印输出冒泡排序后的list

list1 = [89, 13, 67, 99, 14, 90, 35]  # 初始化一个列表
a = Bubble() # 声明一个Bubble类的实例 a
a.bubble_sort(list1) #用实例 a 调用类的方法



"""
冒泡排序
"""
list1 = [89,13,67,99,14,90,35] #初始化一个列表
n = len(list1) #计算列表长度
for i in range(n-1): #循环的排序次数， range(n-1)表示 0，1...n-2，共 n-1 次循环
    for j in range(i+1,n): #每次比对的次数， range(i+1，n) 其中i+1表示每次都是和i后面的数开始比对，一直比到最后一个数 list1[n-1]
        if list1[i] > list1[j]: #如果前面的数比后面的数大
            list1[i],list1[j] = list1[j],list1[i]  #将 list1[i] 和 list1[j] 交换
print(list1) #打印输出冒泡排序后的list





#开一维列表
#方法1使用*运算符
list1 = [0]*10

#方法2列表推导式
list2 = [0 for i in range(10)]

#开二维列表，常用于存图
n = 10 #行
m = 10 #列

#邻接矩阵存图
#下面两种方法都可，推荐使用list3的方法进行初始化
list3 = [[0]*m for i in range(n)]

list4 = [0 for i in range(m)]*n

#邻接表存图
list5 = [[] for i in range(n)]


#使用print()输出，默认情况下结尾会输出换行
print("hello world")
#等价于 print("hello world",end="\n")

#如果不想输出换行
print("hello world",end="")

#简单的拼接输出，默认以空格分隔两个字符串
print("hello","world")

#直接拼接，中间不会有空格
print("hello"+"world")

#数值型与字符串拼接需要将数值强转成字符串才能输出
print(str(123)+"hahaha")

#输出字符串列表，以换行符进行分隔
lst1 = ["hello","world","it's","my","demo"]
print("\n".join(lst1))

#同上的需求，另一种输出的实现方法
print(*lst1,sep="\n")

#输出整数列表，以空格进行分隔
lst2 = {0,1,2,3,4,5}
print(" ".join(map(str,lst2)))

#同上的需求，另一种输出的实现方法
print(*lst2,sep=" ")


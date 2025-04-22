#读入一行字符串
s1 = input()

#读入一行去掉行尾多余空格和制表符的字符串
s2 = input().strip()

#一行只读入一个整数，使用int强转
a = int(input())

#一行只读入一个浮点数，使用float强转
f = float(input())

#一行读入多个字符串，以读入三个字符串为例
s3,s4,s5 = input().split()

#一行读入多个整数，以读入两个整数为例
a1,a2 = map(int,input().split())

#一行读入许多字符串存入列表
lst1 = input().split()

#一行读入许多整数存入列表
lst2 = list(map(int,input().split()))

#一行读入许多整数，并将每个整数-1后存入列表
lst3 = list(map(lambda x: int(x)-1,input().split()))


import sys

input = sys.stdin.readline

def I():
  return input()

def II():
  return int(input())

def FI():
  return float(input())

def LI():
  return input().split()

def MII():
  return map(int,input().split())

def MFI():
  return map(float,input().split())

def LII():
  return list(map(int,input().split()))

def GMI():
  return map(lambda x: int(x)-1,input().split())

def LGMI():
  return list(map(lambda x: int(x)-1,input().split()))

list1 = LI()
list2 = LI()

num1 = int(list1[1])
num2 = int(list2[1])

price1 = float(list1[-1])
price2 = float(list2[-1])

print("VALOR A PAGAR: R$ %.2f"%(num1*price1+num2*price2))
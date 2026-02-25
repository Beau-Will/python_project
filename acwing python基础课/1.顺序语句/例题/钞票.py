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

n = II()

print(n)
print("%d nota(s) de R$ 100,00"%(n//100))
n %= 100
print("%d nota(s) de R$ 50,00"%(n//50))
n %= 50
print("%d nota(s) de R$ 20,00"%(n//20))
n %= 20
print("%d nota(s) de R$ 10,00"%(n//10))
n %= 10
print("%d nota(s) de R$ 5,00"%(n//5))
n %= 5
print("%d nota(s) de R$ 2,00"%(n//2))
n %= 2
print("%d nota(s) de R$ 1,00"%(n//1))
n %= 1
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

print("%d ano(s)"%(n//365))
n %= 365

print("%d mes(es)"%(n//30))
n %= 30

print("%d dia(s)"%(n))
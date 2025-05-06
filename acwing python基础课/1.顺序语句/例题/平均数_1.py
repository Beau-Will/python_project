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

def LII():
  return list(map(int,input().split()))

def GMI():
  return map(lambda x: int(x)-1,input().split())

def LGMI():
  return list(map(lambda x: int(x)-1,input().split()))

a = FI()
b = FI()

print("MEDIA = %.5f"%((a*3.5+b*7.5)/11))
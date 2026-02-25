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

x = FI()
x = int(x*100)

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%(x//10000))
x%=10000
print("%d nota(s) de R$ 50.00"%(x//5000))
x%=5000
print("%d nota(s) de R$ 20.00"%(x//2000))
x%=2000
print("%d nota(s) de R$ 10.00"%(x//1000))
x%=1000
print("%d nota(s) de R$ 5.00"%(x//500))
x%=500
print("%d nota(s) de R$ 2.00"%(x//200))
x%=200
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%(x//100))
x%=100
print("%d moeda(s) de R$ 0.50"%(x//50))
x%=50
print("%d moeda(s) de R$ 0.25"%(x//25))
x%=25
print("%d moeda(s) de R$ 0.10"%(x//10))
x%=10
print("%d moeda(s) de R$ 0.05"%(x//5))
x%=5
print("%d moeda(s) de R$ 0.01"%(x//1))
x%=1
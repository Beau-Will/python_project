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

a,b,c = MFI()

pi = 3.14159

print("TRIANGULO: %.3f"%(a*c/2))
print("CIRCULO: %.3f"%(pi*(c**2)))
print("TRAPEZIO: %.3f"%((a+b)*c/2))
print("QUADRADO: %.3f"%(b**2))
print("RETANGULO: %.3f"%(a*b))
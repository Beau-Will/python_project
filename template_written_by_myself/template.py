import sys

input = sys.stdin.readline

def I():
    return input()

def II():
    return int(input())

def LI():
    return input().split()

def MII():
    return map(int,input().split())

def LII():
    return list(map(int,input().split()))

def LFI():
    return list(map(float,input().split()))

def GMI():
    return map(lambda x: int(x)-1,input().split())

def LGMI():
    return list(map(lambda x: int(x)-1,input().split()))



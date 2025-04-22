#设置模数，a**b=pow(a,b)
P = 10**9+7
#P = pow(10,9)+7

#快速幂,Python自带的pow就是O(logn)的，第三个参数表示模数
a = 2
b = 123456789
ans = pow(a,b,P)

#求逆元，要求P为奇数
n = 2
inv = pow(n,P-2,P)

#求gcd，需要导入math库
import math

gcd = math.gcd(3,6)

#或者这样导入
from math import gcd
gcd2 = gcd(1,4)


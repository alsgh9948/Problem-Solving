import sys

def gcd_func(a,b):
    if b == 0:
        return a
    else:
        return gcd_func(b,a%b)

a, b = map(int, sys.stdin.readline().split())

gcd = gcd_func(a,b)
lcm = int(a*b/gcd)
print(gcd)
print(lcm)
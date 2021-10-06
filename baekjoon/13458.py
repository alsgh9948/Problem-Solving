import math
from sys import stdin

input = stdin.readline

n = int(input())
board = list(map(int, input().split()))
a,b = map(int, input().split())

ans = n
for num in board:
    num -= a
    if num > 0:
        ans += math.ceil(num/b)

print(ans)
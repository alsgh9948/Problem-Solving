from sys import stdin
import bisect
n = int(stdin.readline())

num = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
targets = map(int, stdin.readline().split())
num.sort()

for target in targets:
    idx = bisect.bisect_left(num,target)
    if idx < n and num[idx] == target:
        print(1)
    else:
        print(0)


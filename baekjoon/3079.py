from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
time_table = list(int(input()) for _ in range(n))

def solv():
    left = 1
    right = max(time_table)*m

    while left <= right:
        mid = (left+right)//2

        total = 0
        for t in time_table:
            total += mid//t

        if total >= m:
            right = mid-1
        else:
            left = mid+1
    print(left)

solv()
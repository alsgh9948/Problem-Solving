from sys import stdin
input = stdin.readline

n = int(input())

servers = []
for _ in range(n):
    servers += list(map(int,input().split()))

servers.sort()

def check_start():
    for idx in range(n*n):
        if servers[idx] != 0:
            return idx
    return 0

def solv():
    total = sum(servers)
    target_cnt = total/2
    start = check_start()

    left = 0
    right = servers[-1]

    while left <= right:
        height = (left+right)//2

        cnt = 0
        for idx in range(start,n*n):
            if height >= servers[idx]:
                cnt += servers[idx]
            else:
                cnt += (height*(n*n-idx))
                break
        if cnt >= target_cnt:
            right = height-1
        else:
            left = height+1
    return left

print(solv())
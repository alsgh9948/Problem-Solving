from sys import stdin
from collections import deque
input = stdin.readline
tc = int(input())

def solv():
    global n,q,priority
    n,m = map(int, input().split())
    priority = list(map(int, input().split()))
    q = deque([i for i in range(n-1,-1,-1)])

    cnt = 1
    while q:
        now = q.pop()
        if not priority_check(now):
            q.appendleft(now)
        else:
            if now == m:
                print(cnt)
                break
            priority[now] = 0
            cnt += 1

def priority_check(now):
    for idx in range(n):
        if now == idx:
            continue
        if priority[now] < priority[idx]:
            return False
    return True
for _ in range(tc):
    solv()
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

m = int(input())

network = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)

def solv():
    cnt = 0
    q = deque([0])
    virus = [False]*n
    virus[0] = True

    while q:
        now = q.pop()
        cnt += 1
        for nxt in network[now]:
            if not virus[nxt]:
                virus[nxt] = True
                q.appendleft((nxt))
    return cnt-1

print(solv())
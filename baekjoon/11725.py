from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def solv():
    parents = [0]*(n+1)
    q = deque([1])

    visited = [False]*(n+1)
    visited[1] = True

    while q:
        now = q.pop()

        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                parents[nxt] = now
                q.appendleft(nxt)

    for p in parents[2:]:
        print(p)

solv()
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
network = [[0] for _ in range(n+1)]

start, end = map(int, input().split())

m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    network[b][0] = a
    network[a].append(b)

def solv():
    q = deque([(start,0)])
    visited = [False]*(n+1)

    visited[start] = True

    while q:
        now,cnt = q.pop()

        if now == end:
            return cnt
        parent = network[now][0]
        if parent != 0 and not visited[parent]:
            visited[parent] = True
            q.appendleft((parent,cnt+1))
        for child in network[now][1:]:
            if not visited[child]:
                visited[child] = True
                q.appendleft((child,cnt+1))
    return -1
print(solv())
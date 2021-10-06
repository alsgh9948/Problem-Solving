from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())


max_len = (k+1)*2
def bfs():
    visited = [False]*max_len
    q = deque()
    q.appendleft((n,0))

    while q:
        now,cnt = q.pop()
        if now == k:
            print(cnt)
            return
        visited[now] = True

        if now + 1 < max_len and not visited[now+1]:
            q.appendleft((now+1,cnt+1))
        if now - 1 >= 0 and not visited[now-1]:
            q.appendleft((now-1,cnt+1))
        if (now*2 < max_len and now*2 >= 0) and not visited[now*2]:
            q.appendleft((now*2,cnt+1))
bfs()
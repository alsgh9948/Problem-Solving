from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().strip().split())
ans_time = 1000000
ans_cnt = 0


def bfs():
    visited = [False]*100001
    q = deque()
    q.appendleft((n,0))

    while q:
        now,cnt = q.pop()
        if now == k:
            global ans_time, ans_cnt
            if ans_time > cnt:
                ans_time = cnt
                ans_cnt = 1
            elif ans_time == cnt:
                ans_cnt+=1
            continue
        visited[now] = True

        if now + 1 < 100001 and not visited[now+1]:
            q.appendleft((now+1,cnt+1))
        if now - 1 >= 0 and not visited[now-1]:
            q.appendleft((now-1,cnt+1))
        if (now*2 < 100001 and now*2 >= 0) and not visited[now*2]:
            q.appendleft((now*2,cnt+1))
bfs()
print(ans_time)
print(ans_cnt)
from sys import stdin
from collections import deque

input = stdin.readline
INF = 9876543210

n,q = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in  range(n-1):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

targets = [list(map(int, input().split())) for _ in range(q)]

dist = [[INF]*(n+1) for _ in range(n+1)]
def solv():
    set_dist()
    for k,v in targets:
        answer = 0
        for d in dist[v][1:]:
            if d >= k and d != INF:
                answer += 1

        print(answer)
def set_dist():
    for start in range(1,n+1):
        q = deque([(start, INF)])
        dist[start][start] = 0

        while q:
            now, d = q.pop()
            for nxt,nxt_d in adj_list[now]:
                if dist[start][nxt] == INF:
                    dist[start][nxt] = min(d,nxt_d)
                    q.appendleft((nxt,min(d,nxt_d)))

solv()
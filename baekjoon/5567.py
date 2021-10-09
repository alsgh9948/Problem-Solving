from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def solv():
    print(bfs())

def bfs():
    answer = 0
    visited = [False]*(n+1)
    visited[1] = True

    q = deque([(1,0)])

    while q:
        now,length = q.pop()
        if length == 2:
            continue
        for nxt in adj_list[now]:
            if not visited[nxt]:
                q.appendleft((nxt,length+1))
                visited[nxt] = True
                answer += 1
    return answer

solv()
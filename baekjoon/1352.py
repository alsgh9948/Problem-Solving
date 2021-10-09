from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())

adj_list = [[] for _ in range(n)]
visited = [0]*n
visited_num = 0

for _ in range(m):
    a,b = map(int, input().split())
    adj_list[b-1].append(a-1)
def solv():
    global visited_num
    max_cnt = 0
    max_idx = []
    for start in range(n):
        visited_num += 1
        cnt = bfs(start)
        if max_cnt < cnt:
            max_cnt = cnt
            max_idx = [start+1]
        elif max_cnt == cnt:
            max_idx.append(start+1)

    print(*max_idx)
def bfs(start):
    global visited
    q = deque([start])
    visited[start] = visited_num

    cnt = 0
    while q:
        now = q.pop()
        cnt += 1

        for nxt in adj_list[now]:
            if visited[nxt] != visited_num:
                visited[nxt] = visited_num
                q.appendleft(nxt)
    return cnt
solv()
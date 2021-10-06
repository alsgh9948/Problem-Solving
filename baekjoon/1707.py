import sys
from collections import deque

k = int(sys.stdin.readline())

adj_list = None
visited = None

def bfs(v):
    global visited
    q = deque()

    for start in range(1,v+1):
        if visited[start] != 0:
            continue
        q.appendleft((start,1))
        while q:
            now,color = q.pop()
            visited[now] = color
            for _next in adj_list[now]:
                if visited[_next] == 0:
                    q.appendleft((_next,-color))
                elif visited[_next] == color:
                    return 'NO'


    return 'YES'

def dfs(now, color):
    visited[now] = color
    for _next in adj_list[now]:
        if visited[_next] == 0:
            if not dfs(_next, -color):
                return False
        elif visited[_next] == color:
            return False
    return True

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    adj_list = [[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    # ans = 'YES'
    # for start in range(1,v+1):
    #     if visited[start] == 0:
    #         if not dfs(start,1):
    #             ans = 'NO'
    #             break
    print(bfs(v))


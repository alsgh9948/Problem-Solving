import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# def bfs():
#     rst = 0
#     visited = [False]*(n+1)
#
#     for start in range(1,n+1):
#         if visited[start]:
#             continue
#         rst += 1
#         q = deque()
#         q.appendleft(start)
#
#         while q:
#             now = q.pop()
#             if visited[now]:
#                 continue
#             visited[now] = True
#             for _next in adj_list[now]:
#                 if not visited[_next]:
#                     q.appendleft(_next)
#     return rst
# print(bfs())

visited = [False]*(n+1)
ans = 0

def dfs(visited, now):
    for _next in adj_list[now]:
        if not visited[_next]:
            visited[_next] = True
            dfs(visited,_next)


for start in range(1,n+1):
    if not visited[start]:
        ans += 1
        visited[start] = True
        dfs(visited,start)

print(ans)


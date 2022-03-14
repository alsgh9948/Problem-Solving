from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    adj_list[b].append(a)

visited = [0]*(n+1)
visited_num = 0
def solv():
    answer_count = 0
    answer_vertex = []

    for start in range(1,n+1):
        count = bfs(start)
        if answer_count < count:
            answer_count = count
            answer_vertex = [start]
        elif answer_count == count:
            answer_vertex.append(start)

    answer_vertex.sort()
    print(*answer_vertex)
def bfs(start):
    global visited,visited_num
    visited_num += 1
    q = deque([start])
    visited[start] = visited_num

    count = 0
    while q:
        now = q.pop()

        for nxt in adj_list[now]:
            if visited[nxt] != visited_num:
                visited[nxt] = visited_num
                count += 1
                q.appendleft(nxt)

    return count

solv()
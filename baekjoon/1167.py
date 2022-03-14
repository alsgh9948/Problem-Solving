from sys import stdin
from collections import deque

input = stdin.readline
v = int(input())

adj_list = [[] for _ in range(v+1)]
for _ in range(v):
    input_data = list(map(int, input().split()))
    parent = input_data[0]
    for idx in range(1,len(input_data),2):
        if input_data[idx] == -1:
            break
        child,dist = input_data[idx],input_data[idx+1]
        adj_list[parent].append((child,dist))

answer = 0
def solv():
    global visited
    a = bfs(1,-1)
    b = bfs(a,-1)
    c = bfs(a,b)
    print(c)
def bfs(start,target):
    max_dist = 0
    num = 0
    visited = [False] * (v + 1)

    q = deque([(start,0)])
    visited[start] = True

    while q:
        now,dist = q.pop()

        if target != -1 and now == target:
            return dist

        for nxt, cost in adj_list[now]:
            if not visited[nxt]:
                if max_dist < dist+cost:
                    max_dist = dist+cost
                    num = nxt
                visited[nxt] = True
                q.appendleft((nxt,dist+cost))
    return num
solv()
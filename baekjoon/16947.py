
from sys import stdin,setrecursionlimit
from collections import deque
setrecursionlimit(10000)

n = int(stdin.readline().strip())
train_map = [[] for _ in range(n+1)]
circular_station = [False]*(n+1)
dist = [-1]*(n+1)

for i in range(n):
    a,b = map(int, stdin.readline().strip().split())
    train_map[a].append(b)
    train_map[b].append(a)

visited = [False] * (n + 1)
def solv():
    for start in range(1, n + 1):
        if check_circular(start, start,0):
            break

    for start in range(1, n + 1):
        if circular_station[start]:
            calc_length(start)
    print(*dist[1:])
def calc_length(start):
    global dist
    q = deque()

    q.appendleft((start,0))
    dist[start] = 0
    while q:
        now,length = q.pop()

        for nxt in train_map[now]:
            if dist[nxt] != -1 and dist[nxt] <= length+1:
                continue
            dist[nxt] = length+1
            q.appendleft((nxt,length+1))

def check_circular(start, now, cnt):
    global circular_station,visited

    for nxt in train_map[now]:
        if not visited[nxt]:
            if cnt > 1 and nxt == start:
                circular_station[now] = True
                return True
            visited[nxt] = True

            if check_circular(start, nxt, cnt+1):
                circular_station[now] = True
                return True

            visited[nxt] = False
    return False

solv()
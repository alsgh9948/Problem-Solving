from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []
visited = [[0] * n for _ in range(n)]
visited_num = 0

index = 2
targets = []
for x in range(n):
    board.append(list(input().strip()))
    for y in range(n):
        if board[x][y] == '1':
            board[x][y] = -1
        elif board[x][y] == '0':
            board[x][y] = 0
        elif board[x][y] == 'S':
            board[x][y] = 1
            targets.append((x,y))
        elif board[x][y] == 'K':
            board[x][y] = index
            index += 1
            targets.append((x,y))

parent = [i for i in range(index)]

def solv():
    edges = set_edges()
    edges.sort(key=lambda x:x[2])
    print(kruskal(edges))

def kruskal(edges):
    edge_count = 0
    cost = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            edge_count += 1
            cost += c
            if edge_count == index-2:
                return cost
    return -1
def find(target):
    global parent
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[a] = b

def is_same_parent(a,b):
    return find(a) == find(b)

def set_edges():
    edges = []
    for x,y in targets:
        edges.extend(bfs(x,y))

    return edges
def bfs(sx,sy):
    global visited,visited_num
    start = board[sx][sy]

    q = deque([(sx,sy,0)])

    visited_num += 1
    visited[sx][sy] = visited_num

    edge = []
    while q:
        x,y,cnt = q.pop()

        if board[x][y] > 0 and board[x][y] != start:
            edge.append((start,board[x][y],cnt))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny,cnt+1))
    return edge
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    elif board[x][y] == -1:
        return False
    return True

solv()
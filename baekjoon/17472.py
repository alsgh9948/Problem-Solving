from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
area_edges = [[],[]]

edges = []
parents = []
def solv():
    set_area_num()
    set_edges()
    print(kruskal())

def set_area_num():
    area_num = 2
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                set_area_bfs(x,y,area_num)
                area_num += 1
def set_area_bfs(sx,sy,area_num):
    global board
    q = deque([(sx,sy)])

    edges = []
    board[sx][sy] = area_num

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if boundary_validator(nx,ny):
                if board[nx][ny] == 1:
                    board[nx][ny] = area_num
                    q.appendleft((nx,ny))
                elif board[nx][ny] == 0:
                    edges.append((x, y, d))

    area_edges.append(edges)

def set_edges():
    global parents, edges
    for area_edge in area_edges[2:]:
        for x,y,d in area_edge:
            start = board[x][y]
            end, length = insert_bridge(x,y,d)
            if end != -1:
                edges.append((start,end,length))

    edges.sort(key=lambda x:x[2])
    for i in range(len(area_edges)):
        parents.append(i)

def insert_bridge(x,y,d):
    area_num = board[x][y]
    bridge_length = 0
    while True:
        x += dx[d]
        y += dy[d]
        if bridge_validator(x,y,area_num):
            if board[x][y] != 0:
                if bridge_length >= 2:
                    return board[x][y], bridge_length
                else:
                    return -1, -1
        else:
            return -1, -1

        bridge_length += 1

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

def bridge_validator(x,y,area_num):
    if not boundary_validator(x,y):
        return False
    elif board[x][y] == area_num:
        return False
    return True

def find(target):
    global parents
    if parents[target] == target:
        return target

    parents[target] = find(parents[target])
    return parents[target]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            parents[a] = b
        else:
            parents[b] = a

def is_same_parent(a,b):
    return find(a) == find(b)

def kruskal():
    cost = 0
    edge_count = 0
    for a,b,c in edges:
        if not is_same_parent(a,b):
            union(a,b)
            cost += c
            edge_count += 1
            if edge_count == len(area_edges)-3:
                return cost
    return -1
solv()
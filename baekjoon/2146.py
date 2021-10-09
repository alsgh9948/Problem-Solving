from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
bridge = [[[0,0] for _ in range(n)] for _ in range(n)]
edges = deque()
ans = 987654321
def solv():
    insert_area_num()
    insert_bridge()

def insert_area_num():
    num = 2
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                insert_num_bfs(x,y,num)
                num += 1
def insert_num_bfs(sx,sy,num):
    global board,edges
    q = deque([(sx,sy)])
    board[sx][sy] = num
    while q:
        x,y = q.pop()
        edge_flag = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if board[nx][ny] == 1:
                    board[nx][ny] = num
                    q.appendleft((nx,ny))
                else:
                    edge_flag = True
            else:
                edge_flag = True
        if edge_flag:
            bridge[x][y][0] = num
            edges.appendleft((x,y))
def insert_bridge():
    global edges,bridge, ans
    q_len = len(edges)
    for _ in range(q_len):
        while edges:
            x,y = edges.pop()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx, ny):
                    if board[nx][ny] != 0:
                        continue
                    if bridge[nx][ny][1] == 0:
                        bridge[nx][ny][1] = bridge[x][y][1] + 1
                        bridge[nx][ny][0] = bridge[x][y][0]
                        edges.appendleft((nx,ny))
                    else:
                        if bridge[nx][ny][0] != bridge[x][y][0]:
                            ans = min(ans, bridge[nx][ny][1] + bridge[x][y][1])
    if edges:
        insert_bridge()

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()
print(ans)
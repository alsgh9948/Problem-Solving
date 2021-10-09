from sys import stdin
from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

m,n = map(int, stdin.readline().strip().split())
board = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

room_num = 1
room_num_map = [[0]*m for _ in range(n)]
room_size = [0]
max_extend_room_size = 0
def solv():
    global room_num, room_size
    for i in range(n):
        for j in range(m):
            if room_num_map[i][j] == 0:
                insert_num_bfs(i,j)
                room_num += 1

    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                extend_room_bfs(i,j,visited)

    print(room_num-1)
    print(max(room_size))
    print(max_extend_room_size)
def insert_num_bfs(sx,sy):
    global room_num_map, room_size
    q = deque()
    q.appendleft((sx,sy))
    room_num_map[sx][sy] = room_num
    room_size.append(0)

    while q:
        x,y = q.pop()
        room_size[room_num] += 1
        for d in range(4):
            if board[x][y] & (1<<d):
                continue
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny):
                continue
            elif room_num_map[nx][ny] != 0:
                continue

            room_num_map[nx][ny] = room_num
            q.appendleft((nx,ny))

def extend_room_bfs(sx,sy,visited):
    now_room_num = room_num_map[sx][sy]
    q = deque()

    q.appendleft((sx,sy))
    visited[sx][sy] = True

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx, ny) or visited[nx][ny]:
                continue
            elif room_num_map[nx][ny] != now_room_num:
                global max_extend_room_size
                nxt_room_num = room_num_map[nx][ny]
                max_extend_room_size = max(max_extend_room_size, room_size[now_room_num]+room_size[nxt_room_num])
                continue
            visited[nx][ny] = True
            q.appendleft((nx, ny))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()
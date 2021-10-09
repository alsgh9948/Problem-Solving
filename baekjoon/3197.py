from sys import stdin
from collections import deque
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, stdin.readline().strip().split())

board = []
path_ice_map = [[False]*c for _ in range(r)]
path_ice_cnt = 0

edge_queue = deque()

x1=x2=y1=y2=-1
for i in range(r):
    board.append(list(stdin.readline().strip()))
    for j in range(c):
        if board[i][j] == 'L':
            if x1 == -1:
                x1,y1 = i,j
            else:
                x2,y2 = i,j

def solv():
    check_path()
    # check_edge()

    t = 0
    while True:
        melt_ice()
        t+=1
        if path_ice_cnt == 0:
            return t
def check_path():
    pq = []
    visited = [[None] * c for _ in range(r)]

    heapq.heappush(pq,(0,x1,y1))
    visited[x1][y1] = (-1,-1)

    while pq:
        cnt,x,y = heapq.heappop(pq)
        if x == x2 and y == y2:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue

            visited[nx][ny] = (x,y)
            if board[nx][ny] == 'X':
                heapq.heappush(pq,(cnt+1,nx,ny))
            else:
                heapq.heappush(pq,(cnt,nx,ny))

    global path_ice_map,path_ice_cnt
    x,y = visited[x2][y2]
    while x != -1:
        if board[x][y] == 'X':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx, ny):
                    if board[nx][ny] != 'X':
                        edge_queue.appendleft((x, y))

            path_ice_map[x][y] = True
            path_ice_cnt += 1
        x,y = visited[x][y]

def check_edge():
    global edge_queue

    for x in range(r):
        for y in range(c):
            if board[x][y] == 'X':
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if point_validator(nx,ny):
                        if board[nx][ny] != 'X':
                            edge_queue.appendleft((x,y))
                            break

def melt_ice():
    global edge_queue, path_ice_map, path_ice_cnt
    edge_cnt = len(edge_queue)

    visited = [[False]*c for _ in range(r)]
    for _ in range(edge_cnt):
        x,y = edge_queue.pop()
        board[x][y] = '.'
        if path_ice_map[x][y]:
            path_ice_map[x][y] = False
            path_ice_cnt -= 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny,visited):
                visited[nx][ny] = True
                if board[nx][ny] == 'X':
                    board[nx][ny] = '.'
                    edge_queue.appendleft((nx, ny))
def point_validator(x,y,visited=None):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif visited and visited[x][y]:
        return False
    return True

print(solv())
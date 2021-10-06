from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, stdin.readline().strip().split())

board = [list(stdin.readline().strip()) for _ in range(r)]

n = int(stdin.readline().strip())
h_list = list(map(int, stdin.readline().strip().split()))

def simul():
    global board
    d = -1
    for h in h_list:
        throw_wood(d,r-h)
        d *= -1

def throw_wood(d,x):
    start, end, op = 0, c, 1
    if d == 1:
        start, end, op = c-1,-1,-1

    for y in range(start,end,op):
        if board[x][y] == 'x':
            board[x][y] = '.'
            cluster_check(x,y)
            break

def cluster_check(sx,sy):
    q = deque()
    visited = [[0]*c for _ in range(r)]
    cluster_num = 0
    for d in range(4):
        cluster_num += 1
        edge = []
        mineral_point = []
        floor_status = False

        nx = sx + dx[d]
        ny = sy + dy[d]

        if not point_validator(nx, ny, visited):
            continue

        q.appendleft((nx,ny))
        visited[nx][ny] = cluster_num
        mineral_point.append((nx,ny))
        while q:
            x,y = q.pop()
            if edge_check(x, y):
                edge.append((x,y))
            if x == r - 1:
                floor_status = True

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not point_validator(nx,ny,visited):
                    continue

                q.appendleft((nx,ny))
                visited[nx][ny] = cluster_num
                mineral_point.append((nx,ny))

        if not floor_status:
            move_cluster(edge,mineral_point,visited)
def edge_check(x,y):
    nx = x + dx[1]
    ny = y + dy[1]
    if nx < 0 or ny < 0 or nx >= r or ny >= c:
        return False
    if board[nx][ny] == '.':
        return True
    return False

def move_cluster(edge,mineral_point,visited):
    down_cnt = down_cnt_check(edge,visited)
    move_visited = [[False]*c for _ in range(r)]
    for x,y in mineral_point:
        if not move_visited[x][y]:
            board[x][y] = '.'
        nx = x+down_cnt
        board[nx][y] = 'x'
        move_visited[nx][y] = True

def down_cnt_check(edge,visited):
    min_cnt = 10000000
    for x,y in edge:
        cluster_num = visited[x][y]
        cnt = 0
        for nx in range(x+1,r):
            if nx == r:
                break
            elif board[nx][y] == 'x':
                if visited[nx][y] == cluster_num:
                    cnt = 10000000
                break

            cnt += 1
        min_cnt = min(cnt, min_cnt)
    return min_cnt


def point_validator(x,y,visited = None):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y] == '.':
        return False
    elif visited and visited[x][y] != 0:
        return False
    return True

simul()
for row in board:
    print(''.join(row))

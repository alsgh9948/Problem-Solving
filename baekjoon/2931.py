from sys import stdin
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
block_type = {
    '|':[[-1,0],[1,0]],
    '-':[[0,-1],[0,1]],
    '+':[[-1,0],[1,0],[0,-1],[0,1]],
    '1':[[1,0],[0,1]],
    '2':[[-1,0],[0,1]],
    '3':[[-1,0],[0,-1]],
    '4':[[1,0],[0,-1]]
}

r,c = map(int,input().split())

board = []
mx=my=zx=zy=-1
m_flag=z_flag = False
for x in range(r):
    board.append(list(input()))
    if mx == -1 or zx == -1:
        for y in range(c):
            if mx == -1 and board[x][y] == 'M':
                mx,my = x,y
            if zx == -1 and board[x][y] == 'Z':
                zx,zy = x,y

def solv():
    global m_flag,z_flag
    x,y = search_point(mx,my)
    if x != -1:
        m_flag = True

    x2,y2 = search_point(zx,zy)
    if x2 != -1:
        z_flag = True
    print(x+1,y+1,check_block_type(x,y))

def check_block_type(x,y):
    pipe_dir = []
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,False):
            block = board[nx][ny]
            if block == 'M':
                if not m_flag:
                    pipe_dir.append([dx[d],dy[d]])
            elif block == 'Z':
                if not z_flag:
                    pipe_dir.append([dx[d],dy[d]])
            else:
                tmp_dir = block_type[block]
                tdx = 0 if dx == 0 else dx[d]*-1
                tdy = 0 if dy == 0 else dy[d]*-1
                if [tdx,tdy] in tmp_dir:
                    pipe_dir.append([dx[d],dy[d]])

    return search_block(pipe_dir)

def search_block(pipe_dir):
    for typ in block_type:
        if len(pipe_dir) == len(block_type[typ]):
            flag = True
            for dir in pipe_dir:
                if dir not in block_type[typ]:
                    flag = False
                    break
            if flag:
                return typ

def search_point(sx,sy):
    global m_flag,z_flag
    gx=gy=-1
    q = deque()
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if point_validator(nx, ny):
            block = board[nx][ny]
            tmp_dir = block_type[block]
            tdx = 0 if dx == 0 else dx[d] * -1
            tdy = 0 if dy == 0 else dy[d] * -1
            if [tdx, tdy] in tmp_dir:
                q.appendleft((nx,ny))
                visited[nx][ny] = True
                break

    while q:
        x,y = q.pop()
        block = board[x][y]
        if block in 'MZ':
            continue
        dir = block_type[block]
        for bx,by in dir:
            nx = x + bx
            ny = y + by

            if not visited[nx][ny]:
                if board[nx][ny] == '.':
                    gx,gy = nx,ny
                    continue
                visited[nx][ny] = True
                q.appendleft((nx,ny))
    return gx,gy
def point_validator(x,y,flag=True):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif flag and board[x][y] in ['M','Z','.']:
        return False
    elif not flag and board[x][y] == '.':
        return False
    return True

solv()
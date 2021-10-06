from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
visited_num = 0
visited_rainbow = [[0]*n for _ in range(n)]
visited_rainbow_num = 0

def solv():
    global visited_num
    ans = 0
    while True:
        visited_num += 1
        remove_group_point = set_group()

        if remove_group_point[0] == -1:
            break
        ans += remove_group_point[0]**2
        remove_group(remove_group_point)
        drop_block()
        rotate_board()
        drop_block()
    print(ans)
def set_group():
    global visited_rainbow_num
    remove_group_point = [-1,-1,-1,-1]
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] > 0:
                visited_rainbow_num += 1
                cnt, rainbow_cnt = set_group_bfs(sx,sy)
                if cnt == 1:
                    continue
                remove_group_point = max(remove_group_point, [cnt,rainbow_cnt,sx,sy])
    return remove_group_point

def set_group_bfs(sx,sy):
    global visited,visited_rainbow

    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num
    cnt = 1
    rainbow_cnt = 0
    num = board[sx][sy]
    while q:
        x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,num):
                if board[nx][ny] == num and visited[nx][ny] == visited_num:
                    continue
                elif board[nx][ny] == 0 and visited_rainbow[nx][ny] == visited_rainbow_num:
                    continue
                cnt += 1
                if board[nx][ny] == 0:
                    rainbow_cnt += 1
                visited_rainbow[nx][ny] = visited_rainbow_num
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny))

    return cnt,rainbow_cnt

def remove_group(remove_group_point):
    global board
    cnt,rainbow_cnt,sx,sy = remove_group_point

    q = deque([(sx, sy)])
    num = board[sx][sy]
    board[sx][sy] = -2
    while q:
        x, y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, num):
                board[nx][ny] = -2
                q.appendleft((nx,ny))

def drop_block():
    global board
    for y in range(n):
        step = 0
        for x in range(n-1,-1,-1):
            if board[x][y] == -2:
                step += 1
            elif board[x][y] == -1:
                step = 0
            elif step > 0:
                board[x+step][y],board[x][y] = board[x][y],-2
def rotate_board():
    global board
    tmp = []
    for x in range(n):
        row = []
        for y in range(n):
            row.append(board[x][y])
        tmp.append(row)

    for x in range(n):
        for y in range(n):
            board[n-y-1][x] = tmp[x][y]
def point_validator(x,y,num):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] not in [num, 0]:
        return False
    return True

solv()
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
RAINBOW = 0
BLACK = -1
EMPTY = -2

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited_num = 0

rainbow_visited = [[0]*n for _ in range(n)]
rainbow_visited_num = 0

def solv():
    score = 0
    while True:
        targets = search_group()
        if not targets:
            break
        score += len(targets)**2
        remove_group(targets)

        drop_block()
        rotate_block()
        drop_block()
    print(score)
def rotate_block():
    global board
    new_board = []
    for y in range(n-1,-1,-1):
        row = []
        for x in range(n):
            row.append(board[x][y])
        new_board.append(row)
    board = new_board

def drop_block():
    global board
    for sy in range(n):
        for sx in range(n-2, -1, -1):
            if board[sx][sy] not in [BLACK,EMPTY]:
                x,y = sx+1,sy
                while drop_validator(x,y):
                    x += 1
                if sx != x-1:
                    board[x-1][y],board[sx][sy] = board[sx][sy],EMPTY

def drop_validator(x,y):
    if not boundary_validator(x,y):
        return False
    elif board[x][y] != EMPTY:
        return False
    return True
def remove_group(targets):
    global board
    for x,y in targets:
        board[x][y] = EMPTY

def search_group():
    global visited_num
    visited_num += 1

    targets = []
    rainbow_cnt = 0
    tx,ty = -1,-1
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] > 0 and visited[sx][sy] != visited_num:
                temp_targets,temp_rainbow_cnt = search_group_bfs(sx,sy)
                if len(targets) < len(temp_targets):
                    targets = temp_targets
                    rainbow_cnt = temp_rainbow_cnt
                    tx,ty = sx,sy
                elif len(targets) == len(temp_targets):
                    if rainbow_cnt < temp_rainbow_cnt:
                        targets = temp_targets
                        rainbow_cnt = temp_rainbow_cnt
                        tx,ty = sx,sy
                    elif rainbow_cnt == temp_rainbow_cnt:
                        if sorted(((tx,ty),(sx,sy)))[0] == (tx,ty):
                            targets = temp_targets
                            rainbow_cnt = temp_rainbow_cnt
                            tx, ty = sx, sy
    return targets
def search_group_bfs(sx,sy):
    global visited,rainbow_visited,rainbow_visited_num
    rainbow_visited_num += 1
    q = deque([(sx,sy)])
    target_num = board[sx][sy]

    visited[sx][sy] = visited_num
    targets = []
    rainbow_cnt = 0
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,target_num):
                if board[nx][ny] == RAINBOW:
                    rainbow_cnt += 1
                    rainbow_visited[nx][ny] = rainbow_visited_num
                visited[nx][ny] = visited_num
                targets.append((nx,ny))
                q.appendleft((nx,ny))
    if targets:
        targets.append((sx,sy))
    return targets, rainbow_cnt
def point_validator(x,y,target_num):
    if not boundary_validator(x,y):
        return False
    elif board[x][y] not in [RAINBOW, target_num]:
        return False
    elif board[x][y] == RAINBOW and rainbow_visited[x][y] == rainbow_visited_num:
        return False
    elif board[x][y] == target_num and visited[x][y] == visited_num:
        return False
    return True

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()
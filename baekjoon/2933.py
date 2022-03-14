from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

n = int(input())
command = list(map(int, input().split()))

visited = [[0]*c for _ in range(r)]
visited_num = 0
def solv():
    op = 1
    for h in command:
        sx,sy = throw_wood(h,op)
        if sx != -1:
           drop_targets, check_candidate = divide_mineral(sx,sy)

           if drop_targets:
               drop_count = check_drop_count(check_candidate)
               drop_mineral(drop_targets, drop_count)
        op *= -1
    for row in board:
        print(''.join(row))

def drop_mineral(drop_targets, drop_count):
    global board
    drop_targets.sort(key = lambda x: -x[0])
    for x, y in drop_targets:
        board[x+drop_count][y],board[x][y] = board[x][y],'.'

def check_drop_count(check_candidate):
    drop_count = 987654321
    for x,y in check_candidate:
        num = visited[x][y]
        step = 0
        while True:
            x += 1
            step += 1
            if not boundary_validator(x,y):
                step -= 1
                break
            else:
                if board[x][y] == 'x':
                    if visited[x][y] == num:
                        step = 987654321
                        break
                    step -= 1
                    break
        drop_count = min(drop_count, step)
    return drop_count

def divide_mineral(sx,sy):
    global board, visited_num
    board[sx][sy] = '.'

    for d in range(4):
        visited_num += 1
        nx = sx + dx[d]
        ny = sy + dy[d]

        if point_validator(nx,ny) and board[nx][ny] == 'x':
            drop_targets, check_candidate = divide_check(nx, ny)
            if drop_targets:
                return drop_targets, check_candidate
    return [],[]
def divide_check(sx,sy):
    global visited
    visited[sx][sy] = visited_num
    q = deque([(sx,sy)])
    drop_targets = []
    check_candidate = []

    while q:
        x,y = q.pop()
        drop_targets.append((x, y))

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if d == 1 and board[nx][ny] == '.':
                    check_candidate.append((x,y))
                elif board[nx][ny] == 'x':
                    if nx == r-1:
                        return [],[]
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))
    return drop_targets, check_candidate

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

def point_validator(x,y):
    if not boundary_validator(x,y):
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

def throw_wood(x,op):
    x = r-x
    start = 0
    end = c
    if op == -1:
        start = c-1
        end = -1
    for y in range(start,end,op):
        if board[x][y] == 'x':
            return x,y
    return -1,-1

solv()
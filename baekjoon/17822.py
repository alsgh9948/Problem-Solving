from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,t = map(int, input().split())

board = []
total = 0
total_cnt = n*m
for x in range(n):
    board.append(list(map(int, input().split())))
    total += sum(board[x])

commands = [list(map(int, input().split())) for _ in range(t)]
visited = [[0]*m for _ in range(n)]
visited_num = 0

def solv():
    for command in commands:
        rotate_disk(command)
        renew_disk()
        if total == 0:
            break
    print(total)
def rotate_disk(command):
    global board
    x,d,k = command
    start = x-1
    for target in range(start,n,x):
        op = 1
        if d == 1:
            op = -1
        row = [i for i in board[target]]
        for idx in range(m):
            board[target][(idx+k*op)%m] = row[idx]

def renew_disk():
    global visited_num, total_cnt, total
    visited_num += 1
    flag = False
    for x in range(n):
        for y in range(m):
            if visited[x][y] != visited_num and board[x][y] != 0:
                if bfs(x,y):
                    flag = True

    if not flag:
        avg = total/total_cnt
        for x in range(n):
            for y in range(m):
                if board[x][y] != 0:
                    if board[x][y] > avg:
                        board[x][y] -= 1
                        total -= 1
                        if board[x][y] == 0:
                            total_cnt -= 1
                    elif board[x][y] < avg:
                        board[x][y] += 1
                        total += 1
def bfs(sx,sy):
    global visited, board, total, total_cnt
    remove_target = [(sx,sy)]
    q = deque([(sx,sy)])

    visited[sx][sy] = visited_num
    target = board[sx][sy]
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = (y + dy[d])%m

            if point_validator(nx,ny,target):
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny))
                remove_target.append((nx,ny))

    if len(remove_target) >= 2:
        total_cnt -= len(remove_target)
        total -= target*len(remove_target)

        for x,y in remove_target:
            board[x][y] = 0
        return True
    return False
def point_validator(x,y,target):
    if x < 0 or x >= n:
        return False
    elif board[x][y] != target:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()
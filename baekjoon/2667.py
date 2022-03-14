from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]

def solv():
    num = 1
    answer = []
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] == 1:
                num += 1
                answer.append(bfs(sx,sy,num))

    answer.sort()
    print(len(answer))
    for cnt in answer:
        print(cnt)
def bfs(sx,sy,num):
    global board
    q = deque([(sx,sy)])
    board[sx][sy] = num
    count = 1

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny):
                board[nx][ny] = num
                count += 1
                q.appendleft((nx,ny))
    return count

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] != 1:
        return False
    return True

solv()
from sys import stdin
from collections import deque

input = stdin.readline
qdx = [-1,-1, 0, 1, 1, 1, 0,-1]
qdy = [ 0, 1, 1, 1, 0,-1,-1,-1]

kdx = [-2,-1, 1, 2, 2, 1,-1,-2]
kdy = [ 1, 2, 2, 1,-1,-2,-2,-1]

n,m = map(int, input().split())
board = [[0]*m for _ in range(n)]
cnt = n*m

def solv():
    queen_point = input_data()
    knight_point = input_data()
    input_data()

    queen_check(queen_point)
    knight_check(knight_point)

    print(cnt)

def input_data():
    global board,cnt
    input_data = list(map(int, input().split()))
    point = []
    for idx in range(1,len(input_data),2):
        x = input_data[idx]-1
        y = input_data[idx+1]-1

        board[x][y] = -1
        cnt -= 1
        point.append((x,y))
    return point
def queen_check(queen_point):
    global board, cnt
    for x,y in queen_point:
        for d in range(8):
            nx = x + qdx[d]
            ny = y + qdy[d]
            while point_validator(nx,ny):
                if board[nx][ny] == 0:
                    cnt -= 1
                board[nx][ny] = 1
                nx += qdx[d]
                ny += qdy[d]

def knight_check(knight_point):
    global board, cnt
    for x,y in knight_point:
        for d in range(8):
            nx = x + kdx[d]
            ny = y + kdy[d]

            if point_validator(nx,ny):
                if board[nx][ny] == 0:
                    cnt -= 1
                board[nx][ny] = 1

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == -1:
        return False
    return True

solv()
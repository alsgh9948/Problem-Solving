from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c,n = map(int, input().split())
board = [list(map(lambda x : -1 if x == '.' else 0,input().strip())) for _ in range(r)]

def solv():
    global board

    insert_timing = False
    for _ in range(n):
        insert_target = []
        remove_target = []
        for x in range(r):
            for y in range(c):
                if insert_timing and board[x][y] == -1:
                    insert_target.append((x,y))
                elif board[x][y] != -1:
                    board[x][y] += 1
                    if board[x][y] == 3:
                        remove_target.append((x,y))

        if remove_target:
            remove(remove_target)

        if insert_target:
            insert(insert_target)
        insert_timing = not insert_target

    print_answer()

def print_answer():
    for x in range(r):
        for y in range(c):
            if board[x][y] == -1:
                print('.',end='')
            else:
                print('O',end='')
        print()
def remove(remove_target):
    global board

    for x,y in remove_target:
        board[x][y] = -1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            board[nx][ny] = -1

def insert(insert_target):
    global board

    for x,y in insert_target:
        board[x][y] = 0
solv()
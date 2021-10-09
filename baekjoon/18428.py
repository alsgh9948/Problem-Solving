from sys import stdin
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
board = []
targets = []
teahers = []
for x in range(n):
    board.append(list(input().strip().split()))
    for y in range(n):
        if board[x][y] == 'X':
            targets.append((x,y))
        elif board[x][y] == 'T':
            teahers.append((x,y))

def solv():
    global board
    for comb in combinations(targets,3):
        for x,y in comb:
            board[x][y] = 'O'
        if simul():
            print('YES')
            return
        for x,y in comb:
            board[x][y] = 'X'
    print('NO')
def simul():
    for x,y in teahers:
        for d in range(4):
            if search_student(x,y,d):
                return False
    return True
def search_student(x,y,d):
    while True:
        x += dx[d]
        y += dy[d]

        if not point_validator(x,y):
            return False
        elif board[x][y] == 'O':
            return False
        elif board[x][y] == 'S':
            return True
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()
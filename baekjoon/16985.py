from sys import stdin
from collections import deque
from itertools import permutations

input = stdin.readline
INF = 9876543210

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

origin_board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
visited_num = 0
answer = INF

def solv():
    for order in permutations(range(5)):
        new_board = set_new_board(order)
        make_board(0,new_board)
        if answer == 12:
            break

    print(answer if answer != INF else -1)
def make_board(now,board):
    if now == 5:
        simul(board)
        return
    for _ in range(4):
        board[now] = rotate_board(board[now])
        if (now == 0 and board[0][0][0] == 0) or (now == 4 and board[4][4][4] == 0):
            continue
        else:
            make_board(now + 1, board)
            if answer == 12:
                return

def rotate_board(board):
    new_board = []
    for y in range(4,-1,-1):
        row = []
        for x in range(5):
            row.append(board[x][y])
        new_board.append(row)
    return new_board

def simul(board):
    global visited, visited_num, answer
    q = deque([(0,0,0,0)])

    visited_num += 1
    visited[0][0][0] = visited_num

    while q:
        z,x,y,cnt = q.pop()
        if cnt == answer:
            return

        if (z,x,y) == (4,4,4):
            answer = min(answer, cnt)
            return

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nz,nx,ny,board):
                visited[nz][nx][ny] = visited_num
                q.appendleft((nz,nx,ny,cnt+1))

def point_validator(z,x,y,board):
    if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
        return False
    elif board[z][x][y] == 0:
        return False
    elif visited[z][x][y] == visited_num:
        return False
    return True

def set_new_board(order):
    new_board = []
    for idx in order:
        new_board.append(copy_board(idx))

    return new_board
def copy_board(idx):
    new_board = []
    for x in range(5):
        row = []
        for y in range(5):
            row.append(origin_board[idx][x][y])
        new_board.append(row)
    return new_board

solv()
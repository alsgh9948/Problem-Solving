from sys import stdin
from itertools import permutations
from collections import deque

input = stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
INF = 9876543210

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
visited_num = 0
answer = INF

def solv():
    for order in permutations(range(5),5):
        stack_board(order,0)
    print(answer if answer != INF else -1)
def stack_board(order,idx):
    global board
    if answer == 12:
        return
    if idx == 5:
        simul(order)
        return
    for _ in range(4):
        board_rotate(order[idx])
        stack_board(order,idx+1)

def simul(order):
    global answer,visited,visited_num
    game_board = []
    for idx in order:
        game_board.append(board[idx])

    visited_num += 1

    start = [0,0,0]
    end = [4,4,4]

    if game_board[start[0]][start[1]][start[2]] != 1 or game_board[end[0]][end[1]][end[2]] != 1:
        return

    visited_num += 1
    q = deque([start+[0]])
    visited[0][start[0]][start[1]] = visited_num
    while q:
        z,x,y,cnt = q.pop()

        if cnt >= answer:
            continue
        if end[0] == z and end[1] == x and end[2] == y:
            answer = min(answer,cnt)
            break

        for d in range(6):

            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nz,nx,ny,game_board):
                visited[nz][nx][ny] = visited_num
                q.appendleft((nz,nx,ny,cnt+1))
def point_validator(z,x,y,game_board):
    if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
        return False
    elif game_board[z][x][y] == 0:
        return False
    elif visited[z][x][y] == visited_num:
        return False
    return True

def board_rotate(z):
    global board

    tmp = []
    for row in board[z]:
        tmp_row = []
        for num in row:
            tmp_row.append(num)
        tmp.append(tmp_row)

    for x in range(5):
        for y in range(5):
            board[z][y][4-x] = tmp[x][y]

solv()
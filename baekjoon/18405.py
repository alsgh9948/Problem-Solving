from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,k = map(int, input().split())

board = []

virus = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(n):
        if board[x][y] > 0:
            virus.append((board[x][y],x,y))

virus.sort(reverse=True)
s,tx,ty = map(int, input().split())
def solv():
    global board
    q = deque(virus)
    for _ in range(s):
        q_len = len(q)
        for _ in range(q_len):
            num,x,y = q.pop()
            if x == tx-1 and y == ty-1:
                print(num)
                return

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx,ny):
                    q.appendleft((num,nx,ny))
                    board[nx][ny] = num
        if not q:
            break
    print(board[tx-1][ty-1])

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] != 0:
        return False
    return True
solv()
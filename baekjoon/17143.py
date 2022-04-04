from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

r,c,m = map(int, input().split())

sharks = deque()
board = [[0]*c for _ in range(r)]
for _ in range(m):
    x,y,s,d,z = map(int, input().split())
    sharks.append((x-1,y-1,s,d-1,z))
    board[x-1][y-1] = z
def solv():
    answer = 0

    for y in range(c):
        answer += catch_shark(y)
        move_shark()
    print(answer)

def catch_shark(y):
    global board
    for x in range(r):
        if board[x][y] != 0:
            size = board[x][y]
            board[x][y] = 0
            return size
    return 0

def move_shark():
    global board, sharks

    count_shark = len(sharks)
    for _ in range(count_shark):
        x,y,s,d,z = sharks.pop()
        if board[x][y] != z:
            continue

        board[x][y] = 0
        if d in [0,1]:
            s %= r*2-2
        else:
            s %= c*2-2

        for _ in range(s):
            nx = x + dx[d]
            ny = y + dy[d]

            if not boundary_validator(nx,ny):
                if d in [0,1]:
                    d = (d+1)%2
                else:
                    d = (d+1)%2+2

                nx = x + dx[d]
                ny = y + dy[d]

            x,y = nx,ny
        sharks.appendleft((x,y,s,d,z))

    count_shark = len(sharks)
    for _ in range(count_shark):
        x,y,s,d,z = sharks.pop()
        if board[x][y] < z:
            board[x][y] = z
            sharks.appendleft((x,y,s,d,z))

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True
solv()
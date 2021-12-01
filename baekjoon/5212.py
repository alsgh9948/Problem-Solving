from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

def solv():
    sx,sy,ex,ey = renew_board()

    for row in board[sx:ex+1]:
        print(''.join(row[sy:ey+1]))

def renew_board():
    global board
    sx, sy = r, c
    ex, ey = 0, 0

    remove_targets = []
    for x in range(r):
        for y in range(c):
            if board[x][y] == 'X':
                water_count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if water_check(nx,ny):
                        water_count += 1
                if water_count >= 3:
                    remove_targets.append((x,y))
                else:
                    sx = min(sx,x)
                    sy = min(sy,y)
                    ex = max(ex,x)
                    ey = max(ey,y)

    for x,y in remove_targets:
        board[x][y] = '.'
    return sx,sy,ex,ey

def water_check(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return True
    elif board[x][y] == '.':
        return True
    return False
solv()
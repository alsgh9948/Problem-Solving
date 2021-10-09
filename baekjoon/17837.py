from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

horse_board = [[[] for _ in range(n)] for _ in range(n)]

horses = []

for idx in range(k):
    x,y,d = map(int, input().split())
    horses.append([x-1,y-1,d-1])
    horse_board[x-1][y-1].append(idx)

def solv():
    for t in range(1,1001):
        for idx in range(k):
            if move_horse(idx):
                print(t)
                return
    print(-1)
    return

def move_horse(idx):
    global horse_board
    x,y,d = horses[idx]

    nx = x + dx[d]
    ny = y + dy[d]

    if (nx < 0 or ny < 0 or nx >= n or ny >= n) or board[nx][ny] == 2:
        return blue_area(x,y,d,idx)
    elif board[nx][ny] == 1:
        return red_area(x, y, nx, ny,idx)
    else:
        return white_area(x, y, nx, ny,idx)
def blue_area(x,y,d,idx):
    global horse_board

    if d in [0, 1]:
        d = (d + 1) % 2
    else:
        d = ((d + 1) % 2) + 2

    nx = x + dx[d]
    ny = y + dy[d]
    horses[idx][2] = d
    if (nx < 0 or ny < 0 or nx >= n or ny >= n) or board[nx][ny] == 2:
        return False

    if board[nx][ny] == 1:
        return red_area(x,y,nx,ny,idx)
    else:
        return white_area(x,y,nx,ny,idx)
def red_area(x,y,nx,ny,idx):
    global horse_board, horses
    target_idx = 0
    for i in range(len(horse_board[x][y])):
        if horse_board[x][y][i] == idx:
            target_idx = i
            break

    tmp = horse_board[x][y][target_idx:]
    tmp.reverse()

    cnt = 0
    for i in tmp:
        cnt+=1
        horses[i][0] = nx
        horses[i][1] = ny
        horse_board[nx][ny].append(i)

    for _ in range(cnt):
        horse_board[x][y].pop()

    if len(horse_board[nx][ny]) >= 4:
        return True
    return False

def white_area(x,y,nx,ny,idx):
    global horse_board, horses
    target_idx = 0
    for i in range(len(horse_board[x][y])):
        if horse_board[x][y][i] == idx:
            target_idx = i
            break
    cnt = 0
    for i in horse_board[x][y][target_idx:]:
        cnt += 1
        horses[i][0] = nx
        horses[i][1] = ny
        horse_board[nx][ny].append(i)

    for _ in range(cnt):
        horse_board[x][y].pop()

    if len(horse_board[nx][ny]) >= 4:
        return True
    return False

solv()
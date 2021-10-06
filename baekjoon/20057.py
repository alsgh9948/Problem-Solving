from sys import stdin

input = stdin.readline
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def solv():
    x = n//2
    y = n//2
    cnt = 0
    typ = 1
    typ_cnt = 0
    d = 0
    while True:
        if x == 0 and y == 0:
            return
        if typ == cnt:
            d = (d+1)%4
            cnt = 0
            typ_cnt += 1

            if typ_cnt == 2:
                typ += 1
                typ_cnt = 0
        x += dx[d]
        y += dy[d]
        cnt += 1
        spread_send(x,y,d)

def spread_send(x,y,d):
    global board, ans
    send = board[x][y]
    total = 0
    total += spread_left_right(x,y,d,'r',send)
    total += spread_left_right(x,y,d,'l',send)
    spread_front(x,y,d,send,total)

def spread_front(sx,sy,d,send,total):
    global ans
    nx = sx + dx[d]*2
    ny = sy + dy[d]*2
    if point_validator(nx,ny):
        board[nx][ny] += int(send*0.05)
    else:
        ans += int(send*0.05)
    total += int(send*0.05)

    nx = sx + dx[d]
    ny = sy + dy[d]
    board[sx][sy] = 0
    remain_send = send - total
    if point_validator(nx, ny):
        board[nx][ny] += remain_send
    else:
        ans += remain_send
def spread_left_right(sx,sy,td,typ,send):
    global ans
    total_send = 0
    if typ == 'r':
        d = (td + 3) % 4
    else:
        d = (td + 1) % 4

    x = sx + dx[d]
    y = sy + dy[d]
    if point_validator(x, y):
        board[x][y] += int(send * 0.07)
    else:
        ans += int(send * 0.07)
    total_send += int(send * 0.07)

    nx = x + dx[d]
    ny = y + dy[d]
    if point_validator(nx, ny):
        board[nx][ny] += int(send * 0.02)
    else:
        ans += int(send * 0.02)
    total_send += int(send*0.02)

    if typ == 'r':
        left = 0.1
        right = 0.01
    else:
        left = 0.01
        right = 0.1

    nd = (d + 1) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if point_validator(nx, ny):
        board[nx][ny] += int(send * left)
    else:
        ans += int(send * left)
    total_send += int(send * left)

    nd = (d + 3) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if point_validator(nx, ny):
        board[nx][ny] += int(send * right)
    else:
        ans += int(send * right)
    total_send += int(send * right)

    return total_send

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()
print(ans)


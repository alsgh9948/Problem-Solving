from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def solv():
    simul()
    print(answer)

def simul():
    max_move_cnt = 1
    rotate_cnt = 0
    d = 3

    x = y = n//2
    while True:
        for _ in range(max_move_cnt):
            before_send = board[x][y]
            x += dx[d]
            y += dy[d]

            spread_send(x,y,d)
            board[x][y] = before_send

            if x == 0 and y == 0:
                return

        d = (d-1)%4
        rotate_cnt += 1
        if rotate_cnt == 2:
            rotate_cnt = 0
            max_move_cnt += 1

def spread_send(x,y,d):
    global board
    now_send = board[x][y]

    total = spread_side(x,y,d,now_send)
    spread_front(x,y,d,now_send,total)

def spread_side(sx,sy,dir,send):
    global board, answer

    total = 0
    for typ in [1,-1]:
        nd = (dir+typ)%4
        x = sx+dx[nd]
        y = sy+dy[nd]
        if boundary_validator(x,y):
            board[x][y] += int(send*0.07)
        else:
            answer += int(send*0.07)
        total += int(send * 0.07)

        for d,op in [(-1*typ,0.1),(0,0.02),(1*typ,0.01)]:
            nx = x + dx[(nd+d)%4]
            ny = y + dy[(nd+d)%4]
            if boundary_validator(nx,ny):
                board[nx][ny] += int(send*op)
            else:
                answer += int(send*op)
            total += int(send*op)

    return total

def spread_front(x,y,d,send,total):
    global board, answer

    nx = x + dx[d]*2
    ny = y + dy[d]*2
    if boundary_validator(nx,ny):
        board[nx][ny] += int(send*0.05)
    else:
        answer += int(send*0.05)
    total += int(send*0.05)

    nx = x + dx[d]
    ny = y + dy[d]
    alpha = send-total
    if boundary_validator(nx,ny):
        board[nx][ny] += alpha
    else:
        answer += alpha

def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()
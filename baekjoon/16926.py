from sys import stdin
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m,r = map(int, stdin.readline().split())

board = [list(stdin.readline().split()) for _ in range(n)]

def solv():
    global board
    for _ in range(r):
        for size in range(min(n,m)//2):
            sx,sy = size,size
            ex,ey = n-size,m-size

            d = 0
            temp = board[sx][sy]
            nx,ny = sx+dx[d], sy+dy[d]
            while True:
                board[nx][ny], temp = temp, board[nx][ny]
                nx += dx[d]
                ny += dy[d]

                if nx < sx or ny < sy or nx >= ex or ny >= ey:
                    nx -= dx[d]
                    ny -= dy[d]

                    d += 1
                    if d == 4:
                        break

                    nx += dx[d]
                    ny += dy[d]

solv()

for row in board:
    print(*row)

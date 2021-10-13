dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
target = int(input())

def solv():
    board = [[0] * n for _ in range(n)]
    x,y,d = 0,0,0
    num = n*n
    tx=ty=-1
    while True:
        board[x][y] = num
        if num == target:
            tx,ty=x,y
        num -= 1
        x,y,d = calc_next(x,y,d,board)
        if x == -1:
            break
    for row in board:
        print(*row)
    print(tx+1,ty+1)
def calc_next(x,y,d,board):
    for _ in range(2):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validate(nx,ny,board):
            return nx,ny,d
        d = (d+1)%4
    return -1,-1,-1
def point_validate(x,y,board):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] != 0:
        return False
    return True
solv()
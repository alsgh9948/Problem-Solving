dx = [0, -1, 0]
dy = [-1, 0, 1]

def solv(t):
    global board
    input()
    board = [list(map(int, input().split())) for _ in range(100)]

    sx = 99
    sy = board[99].index(2)
    print('#%d %d'%(t, simul(sx,sy)))
def simul(x,y):
    while x != 0:
        d = check_side(x,y)
        if d in [0,2]:
            x,y = move_side(x,y,d)
        else:
            x += dx[d]
            y += dy[d]
    return y
def move_side(x,y,d):
    while 0 <= y <= 99 and board[x][y] == 1:
        y += dy[d]
    y -= dy[d]
    x -= 1
    return x,y
def check_side(x,y):
    if y not in [0,99]:
        if board[x][y+1] == 1:
            return 2
        elif board[x][y-1] == 1:
            return 0
        else:
            return 1
    elif y == 0 and board[x][y+1] == 1:
            return 2
    elif y == 99 and board[x][y-1] == 1:
            return 0
    else:
        return 1

for t in range(1,11):
    solv(t)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
if n > 0:
    input_str = input().strip()

board = [[0]*100 for _ in range(100)]
def solv():
    global board
    x=y=sx=sy=ex=ey=50
    d=2
    board[x][y] = 1
    for op in input_str:
        x,y,d = operation(op, x, y, d)

        sx = min(sx, x)
        sy = min(sy, y)

        ex = max(ex, x)
        ey = max(ey, y)

        board[x][y] = 1
    print_ans(sx,sy,ex,ey)

def print_ans(sx,sy,ex,ey):
    for x in range(sx,ex+1):
        for y in range(sy,ey+1):
            if board[x][y]==1:
                print('.',end='')
            else:
                print('#',end='')
        print()
def operation(op,x,y,d):
    if op == 'F':
        x += dx[d]
        y += dy[d]
    elif op == 'R':
        d = (d+1)%4
    else:
        d = (d+3)%4
    return x,y,d

if n > 0:
    solv()
else:
    print('.')
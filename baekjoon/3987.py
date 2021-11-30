from sys import stdin

input = stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
INF = 9876543210

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

sx,sy = map(lambda x:int(x)-1, input().split())

def solv():
    answer = [0,'-']
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]
        if point_validator(nx,ny):
            simul_result = simul(sx,sy,nx,ny,d)
            if simul_result > answer[0]:
                answer = [simul_result,'URDL'[d]]
                if answer[0] == INF:
                    print('URDL'[d])
                    print('Voyager')
                    return
    print(answer[1])
    print(answer[0])
def simul(sx,sy,tx,ty,td):
    count = 1
    x,y,d=tx,ty,td
    while point_validator(x,y):
        if board[x][y] == 'C':
            break
        else:
            d = trans_dir(x,y,d)
            if (x,y,d) == (sx,sy,td):
                return INF
            x += dx[d]
            y += dy[d]
            count += 1
    return count
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
def trans_dir(x,y,d):
    if board[x][y] == '/':
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2
    elif board[x][y] == '\\':
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        elif d == 3:
            return 0
    else:
        return d
solv()
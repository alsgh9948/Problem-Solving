from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = []
air_conditioner = []

for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 9:
            air_conditioner.append((x,y))

visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
def solv():

    for sx,sy in air_conditioner:
        for sd in range(4):
            if not visited[sx][sy][(sd+2)%4] and not visited[sx][sy][sd]:
                simul(sx,sy,sd)
        visited[sx][sy] = [True,True,True,True]

    answer = 0
    for x in range(n):
        for y in range(m):
            if True in visited[x][y]:
                answer += 1
    print(answer)
def simul(sx,sy,sd):
    global visited
    x,y,d = sx,sy,sd
    while True:
        x += dx[d]
        y += dy[d]

        if point_validator(x,y,d):
            visited[x][y][d] = True
            d = rotate_dir(board[x][y],d)
            if d == -1:
                break
        else:
            break
def rotate_dir(typ,d):
    if typ in [0,9]:
        return d
    elif typ == 1:
        if d in [1,3]:
            return -1
        else:
            return d
    elif typ == 2:
        if d in [0,2]:
            return -1
        else:
            return d
    elif typ == 3:
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        else:
            return 2
    elif typ == 4:
        if d == 0:
            return 3
        elif d == 1:
            return 2
        elif d == 2:
            return 1
        else:
            return 0
def point_validator(x,y,d):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y][d]:
        return False
    return True
solv()
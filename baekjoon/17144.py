from sys import stdin

dx = [
    [0,-1,0,1],
    [0,1,0,-1]
]
dy = [
    [1,0,-1,0],
    [1,0,-1,0]
]

r,c,t = map(int, stdin.readline().split())

board = []
air = []
for i in range(r):
    input_data = list(map(int,stdin.readline().split()))
    row = []
    for j in range(c):
        row.append([input_data[j],0])
        if input_data[j] == -1:
            air.append((i,j))
            row[j][1] = -1
    board.append(row)

def solv():
    typ = 0
    for _ in range(t):
        spred(typ)
        clean_air()
        typ = (typ+1)%2
    ans = 2
    for row in board:
        for amount in row:
            ans += amount[typ]
    print(ans)
def spred(typ):
    global board
    for x in range(r):
        for y in range(c):
            if board[x][y][typ] > 0:
                nxt_typ = (typ+1)%2
                spred_amount = board[x][y][typ] // 5
                if spred_amount > 0:
                    for d in range(4):
                        nx = x + dx[0][d]
                        ny = y + dy[0][d]

                        if point_validator(nx,ny):
                            board[x][y][typ] -= spred_amount
                            board[nx][ny][nxt_typ] += spred_amount

                board[x][y][nxt_typ] += board[x][y][typ]
                board[x][y][typ] = 0

def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y][0] == -1:
        return False
    return True


def clean_air():
    rotate(air[0][0],air[0][1]+1,0)
    board[air[0][0]][air[0][1]] = [-1,-1]
    rotate(air[1][0],air[1][1]+1,1)
    board[air[1][0]][air[1][1]] = [-1,-1]


def rotate(x,y,rotate_dir):
    global board
    d = 0

    tmp = [0,0]
    while True:
        if board[x][y][0] == -1:
            return
        board[x][y], tmp = [tmp[0],tmp[1]], [board[x][y][0],board[x][y][1]]

        x += dx[rotate_dir][d]
        y += dy[rotate_dir][d]

        if not rotate_validator(x,y,rotate_dir):
            x -= dx[rotate_dir][d]
            y -= dy[rotate_dir][d]

            d = (d+1)%4

            x += dx[rotate_dir][d]
            y += dy[rotate_dir][d]

def rotate_validator(x,y,rotate_dir):
    if rotate_dir == 0 and (x < 0 or y < 0 or x > air[0][0] or y >= c):
        return False
    elif rotate_dir == 1 and (x < air[1][0] or y < 0 or x >= r  or y >= c):
        return False
    return True
solv()
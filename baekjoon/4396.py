dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]

n = int(input())

mine = [list(input().strip()) for _ in range(n)]
board = [list(input().strip()) for _ in range(n)]

def solv():
    flag = False
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'x':
                if mine[x][y] == '*':
                    flag = True
                search_mine(x,y)

    if flag:
        check_mine()

    for row in board:
        print(''.join(row))

def check_mine():
    for x in range(n):
        for y in range(n):
            if mine[x][y] == '*':
                board[x][y] = '*'
def search_mine(x,y):
    global board
    cnt = 0
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validate(nx, ny):
            if mine[nx][ny] == '*':
                cnt += 1
    board[x][y] = str(cnt)
def point_validate(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True
solv()
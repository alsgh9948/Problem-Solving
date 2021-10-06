from sys import stdin

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int, stdin.readline().split())
board = []

w_list = []
for i in range(r):
    board.append(list(stdin.readline()))
    for j in range(c):
        if board[i][j] == 'W':
            w_list.append((i,j))

def solv():
    global board
    for x,y in w_list:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] == 'W':
                continue
            if board[nx][ny] == 'S':
                return 0

            board[nx][ny] = 'D'
    return 1
ans = solv()
print(ans)
if ans == 1:
    for row in board:
        print(''.join(row),end='')
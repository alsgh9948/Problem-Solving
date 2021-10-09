dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c,k = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]

answer = 0
def solv():
    board[r-1][0] = 'T'
    dfs(r-1,0,1)
    print(answer)
def dfs(x,y,cnt):
    global answer,board
    if (x,y) == (0,c-1):
        if cnt == k:
            answer += 1
        return
    if cnt >= k:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny):
            board[nx][ny] = 'T'
            dfs(nx,ny,cnt+1)
            board[nx][ny] = '.'
def point_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    elif board[x][y] != '.':
        return False
    return True

solv()
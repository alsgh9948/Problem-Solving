from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def init():
    global n, m, board, ans,empty_cnt

    tc = 1
    while True:
        try:
            ans = 987654321
            empty_cnt = 0
            n,m = map(int, input().split())
            board = []
            for x in range(n):
                board.append(input().strip())
                for y in range(m):
                    if board[x][y] == '.':
                        empty_cnt += 1
            solv()
            print('Case %d: %d'%(tc,-1 if ans == 987654321 else ans))
            tc += 1
        except:
            break

def solv():
    visited = [[False]*m for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            if board[sx][sy] == '.':
                visited[sx][sy] = True
                dfs(sx,sy,0,1,visited)
                visited[sx][sy] = False

def dfs(x,y,cnt,visited_cnt,visited):
    global ans
    if visited_cnt == empty_cnt:
        ans = min(ans,cnt)
        return

    if cnt >= ans:
        return

    for d in range(4):
        nx,ny,move_cnt = move_ball(x,y,d,visited)
        if move_cnt > 0:
            dfs(nx,ny,cnt+1,visited_cnt+move_cnt,visited)
            back_ball(nx,ny,d,move_cnt,visited)
def move_ball(x,y,d,visited):
    nx = x
    ny = y
    cnt = 0
    while True:
        nx += dx[d]
        ny += dy[d]

        if not point_validator(nx,ny,visited):
            nx -= dx[d]
            ny -= dy[d]
            return nx,ny,cnt
        cnt += 1
        visited[nx][ny] = True

def back_ball(x,y,d,cnt,visited):
    visited[x][y] = False
    for _ in range(cnt-1):
        x -= dx[d]
        y -= dy[d]
        visited[x][y] = False

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] == '*':
        return False
    return True

init()
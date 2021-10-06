n = int(input())

dx = [0,1,1]
dy = [1,1,0]

board = [list(map(int, input().strip().split())) for _ in range(n)]

ans = 0

dp = [[[-1,-1,-1] for _ in range(n)] for _ in range(n)]

def dfs(x,y,dir):
    global dp
    if x == n-1 and y == n-1:
        return 1

    cnt = 0
    for d in range(3):
        if (dir == 0 and d == 2) or (dir == 2 and d == 0):
            continue
        nx = x + dx[d]
        ny = y + dy[d]

        if not point_validator(nx,ny):
            continue
        if d == 1:
            nx2 = x + dx[0]
            ny2 = y + dy[0]

            nx3 = x + dx[2]
            ny3 = y + dy[2]

            if not point_validator(nx2, ny2) or not point_validator(nx3,ny3):
                continue
        if dp[nx][ny][d] != -1:
           cnt += dp[nx][ny][d]
        else:
            cnt += dfs(nx,ny,d)
    dp[x][y][dir] = cnt
    return cnt
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 1:
        return False
    return True

if board[n-1][n-1] == 1:
    print(0)
else:
    ans = dfs(0,1,0)
    print(ans)
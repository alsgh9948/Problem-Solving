dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int,input().strip().split())

board = [input() for _ in range(r)]

alpha = [False]*26
ans = -1

def point_check(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

def dfs(cnt, x, y):
    global alpha,ans
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not point_check(nx,ny) or alpha[ord(board[nx][ny]) - ord('A')]:
            continue
        alpha[ord(board[nx][ny])-ord('A')] = True
        dfs(cnt+1,nx,ny)
        alpha[ord(board[nx][ny])-ord('A')] = False

alpha[ord(board[0][0]) - ord('A')] = True
dfs(1,0,0)
print(ans)
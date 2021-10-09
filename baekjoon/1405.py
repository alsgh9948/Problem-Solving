dx = [0,0,1,-1]
dy = [1,-1,0,0]

input_str = list(map(int, input().split()))

n = input_str[0]
dir_p = []

for p in input_str[1:]:
    dir_p.append(p/100)
ans = 0

def solv():
    sx=sy=50
    visited = [[False] * 100 for _ in range(100)]
    visited[sx][sy] = True
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(1,nx,ny,visited,dir_p[d])
            visited[nx][ny] = False

    print(ans)
def dfs(cnt,x,y,visited,p):
    global ans
    if cnt == n:
        ans += p
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(cnt+1,nx,ny,visited,p*dir_p[d])
            visited[nx][ny] = False

solv()
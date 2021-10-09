from sys import stdin,setrecursionlimit
dir = {
    'U':[-1,0],
    'D':[1,0],
    'R':[0,1],
    'L':[0,-1]
}

n,m = map(int, stdin.readline().split())

board = [stdin.readline() for _ in range(n)]
is_exit = [[0]*m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def solv():
    ans = 0
    for i in range(n):
        for j in range(m):
            if is_exit[i][j] == 0:
                ans += start(i,j)

    return ans

def start(sx,sy):
    global is_exit, visited
    path = [(sx,sy)]
    visited[sx][sy] = True
    rst = 0
    cnt = 0
    while True:
        x,y = path[-1]
        d = board[x][y]
        nx = x + dir[d][0]
        ny = y + dir[d][1]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            rst = 1
            break
        elif visited[nx][ny]:
            rst = 2
            break
        else:
            if is_exit[nx][ny] == 0:
                visited[nx][ny] = True
                path.append((nx,ny))
            else:
                rst = is_exit[nx][ny]
                break

    for x,y in path:
        is_exit[x][y] = rst
        visited[x][y] = False
        if rst == 1:
            cnt += 1

    return cnt
print(solv())
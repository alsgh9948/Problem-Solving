dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())

def solv(t):
    global n,k,board,answer
    n,k = map(int, input().split())

    board = []
    start_height = 0
    answer = 0
    for x in range(n):
        board.append(list(map(int, input().split())))
        start_height = max([start_height]+board[x])

    simul(start_height)
    print('#%d %d'%(t,answer))
def simul(start_height):
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == start_height:
                visited[x][y] = 1
                dfs(visited,x,y,False)
                visited[x][y] = 0

def dfs(visited,x,y,flag):
    global board, answer
    answer = max(answer, visited[x][y])
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if point_validator(nx,ny,visited):
            if board[nx][ny] >= board[x][y]:
                if not flag and board[nx][ny] - board[x][y] + 1 <= k:
                    tmp = board[nx][ny]
                    board[nx][ny] = board[x][y]-1
                    visited[nx][ny] = visited[x][y] + 1
                    dfs(visited,nx,ny,True)
                    board[nx][ny] = tmp
            else:
                visited[nx][ny] = visited[x][y] + 1
                dfs(visited,nx,ny,flag)
            visited[nx][ny] = 0

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] != 0:
        return False
    return True
for t in range(1, tc+1):
    solv(t)
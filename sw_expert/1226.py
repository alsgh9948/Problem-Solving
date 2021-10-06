from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0]*16 for _ in range(16)]
visited_num = 0
def solv(t):
    global board
    input()
    board = []
    sx=sy=-1
    for x in range(16):
        board.append(input().strip())
        if sx == -1:
            for y in range(16):
                if board[x][y] == '2':
                    sx,sy = x,y

    print('#%d %d'%(t,bfs(sx,sy)))

def bfs(sx,sy):
    global visited
    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num

    while q:
        x,y = q.pop()

        if board[x][y] == '3':
            return 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny))
    return 0

def point_validator(x,y):
    if x < 0 or y < 0 or x >= 16 or y >= 16:
        return False
    elif board[x][y] == '1':
        return False
    elif visited[x][y] == visited_num:
        return False
    return True
for t in range(1,11):
    visited_num += 1
    solv(t)
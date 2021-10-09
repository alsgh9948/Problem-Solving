from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(stdin.readline().strip())

board = [stdin.readline().strip() for _ in range(n)]

visited = [[[False,False] for _ in range(n)] for _ in range(n)]
normal_ans = 0
abnormal_ans = 0
def solv():
    for i in range(n):
        for j in range(n):
            bfs(i,j)

    print(normal_ans,abnormal_ans)
def bfs(sx,sy):
    global visited,normal_ans, abnormal_ans
    q = deque()

    if not visited[sx][sy][0]:
        q.appendleft((sx,sy,0))
        visited[sx][sy][0] = True
        normal_ans += 1

    if not visited[sx][sy][1]:
        q.appendleft((sx,sy,1))
        visited[sx][sy][1] = True
        abnormal_ans += 1

    while q:
        x,y,status = q.pop()
        now_color = board[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,status,now_color):
                continue

            visited[nx][ny][status] = True
            q.appendleft((nx,ny,status))
def point_validator(x,y,status,now_color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y][status]:
        return False

    nxt_color = board[x][y]
    if status == 0:
        if now_color != nxt_color:
            return False
    else:
        if now_color == 'B':
            if nxt_color != 'B':
                return False
        else:
            if nxt_color == 'B':
                return False
    return True

solv()
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

def solv():
    q = deque([(0,0,0)])
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

    visited[0][0][0] = 1
    answer = 9876543210
    while q:
        q_len = len(q)
        for _ in range(q_len):
            x,y,wall_cnt = q.pop()
            cnt = visited[x][y][wall_cnt]

            if x == n - 1 and y == m - 1:
                answer = min(answer,visited[x][y][wall_cnt])
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if point_validator(nx,ny):
                    if board[nx][ny] == '1':
                        if wall_cnt < k:
                            if cnt%2 == 0 and (visited[nx][ny][wall_cnt+1] == 0 or visited[nx][ny][wall_cnt+1] > cnt+2):
                                q.appendleft((nx,ny,wall_cnt+1))
                                visited[nx][ny][wall_cnt+1] = cnt+2
                            elif cnt%2 == 1 and (visited[nx][ny][wall_cnt+1] == 0 or visited[nx][ny][wall_cnt+1] > cnt+1):
                                q.appendleft((nx,ny,wall_cnt+1))
                                visited[nx][ny][wall_cnt+1] = cnt+1
                    else:
                        if visited[nx][ny][wall_cnt] == 0 or visited[nx][ny][wall_cnt] > cnt+1:
                            visited[nx][ny][wall_cnt] = cnt+1
                            q.appendleft((nx,ny,wall_cnt))
    print(-1 if answer == 9876543210 else answer)

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
solv()
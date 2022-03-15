from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []
candidates = []

for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 0:
            candidates.append((x,y))

visited = [[0]*m for _ in range(n)]
visited_num = 0
def solv():
    global board, visited_num
    answer = 0

    for p1,p2 in combinations(candidates,2):
        visited_num += 1
        board[p1[0]][p1[1]] = board[p2[0]][p2[1]] = 1

        cnt = simul(p1[0],p1[1])
        cnt += simul(p2[0],p2[1])
        board[p1[0]][p1[1]] = board[p2[0]][p2[1]] = 0

        answer = max(cnt, answer)
    print(answer)

def simul(sx,sy):
    cnt = 0
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if point_validator(nx,ny) and board[nx][ny] == 2:
            cnt += bfs(nx,ny)
    return cnt

def bfs(sx,sy):
    global visited
    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num
    cnt = 1

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny):
                if board[nx][ny] == 2:
                    visited[nx][ny] = visited_num
                    cnt += 1
                    q.appendleft((nx,ny))
                elif board[nx][ny] == 0:
                    return 0
    return cnt
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()

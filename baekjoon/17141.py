from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 9876543210

n,m = map(int, input().split())
board = []
virus = []
visited = [[False]*n for _ in range(n)]
visited_num = 0

empty_cnt = 0

for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(n):
        if board[x][y] == 2:
            virus.append((x,y))
        if board[x][y] != 1:
            empty_cnt += 1

def solv():
    global visited, visited_num
    answer = INF

    for comb in combinations(virus,m):
        visited_num += 1
        for x,y in comb:
            visited[x][y] = visited_num
        q = deque(comb)
        answer = min(answer, bfs(q))

    print(answer if answer != INF else -1)

def bfs(q):
    global visited
    cnt = 0
    t = 0
    while q:
        q_len = len(q)
        t += 1
        for _ in range(q_len):
            x,y = q.pop()
            cnt += 1

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx,ny):
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))
    if empty_cnt == cnt:
        return t-1
    else:
        return INF

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 1:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()

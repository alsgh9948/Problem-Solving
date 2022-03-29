from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,g,r = map(int, input().split())

board = []
candidates = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 2:
            candidates.append((x,y))

answer = 0
def solv():
    for candidate in combinations(candidates, g+r):
       select_color([r,g],[],candidate)
    print(answer)

def select_color(cnt,order,candidate):
    if cnt == [0,0]:
        simul(candidate,order)
        return

    if cnt[0] > 0:
        order.append('R')
        cnt[0] -= 1
        select_color(cnt,order,candidate)
        cnt[0] += 1
        order.pop()

    if cnt[1] > 0:
        order.append('G')
        cnt[1] -= 1
        select_color(cnt,order,candidate)
        cnt[1] += 1
        order.pop()
def simul(candidate,order):
    global answer

    q = deque()
    visited = [[[0, ''] for _ in range(m)] for _ in range(n)]
    visited_num = 1

    for idx in range(g + r):
        x, y = candidate[idx]
        q.appendleft((x, y, order[idx]))
        visited[x][y] = [visited_num, order[idx]]

    flower_count = 0
    while q:
        q_len = len(q)
        visited_num += 1
        for _ in range(q_len):
            x,y,typ = q.pop()

            if visited[x][y][0] == -1:
                flower_count += 1
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if boundary_validator(nx,ny,visited):
                    if visited[nx][ny][0] == 0:
                        visited[nx][ny] = [visited_num,typ]
                        q.appendleft((nx,ny,typ))
                    elif visited[nx][ny][0] == visited_num and visited[nx][ny][1] != typ:
                        visited[nx][ny][0] = -1
    answer = max(answer, flower_count)
def boundary_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 0:
        return False
    elif visited[x][y][0] == -1:
        return False
    return True
solv()

from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []
candidate = []
virus = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 0:
            candidate.append((x,y))
        elif board[x][y] == 2:
            virus.append((x,y))

visited_num = 2
def solv():
    global board, visited_num
    answer = 0
    for comb in combinations(candidate,3):
        for x,y in comb:
            board[x][y] = 1

        visited_num += 1
        answer = max(answer, len(candidate) - 3 - bfs())
        for x,y in comb:
            board[x][y] = 0

    print(answer)

def bfs():
    global board
    q = deque(virus)

    cnt = 0
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[nx][ny] = visited_num
                cnt += 1
                q.appendleft((nx,ny))

    return cnt


def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] in [1,2,visited_num]:
        return False
    return True

solv()
from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
board = []
visited = [[0]*m for _ in range(n)]
visited_num = 0
candidate = []
answer = 0

for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 0:
            candidate.append((x,y))

def solv():
    global board,answer,visited_num
    for p1,p2 in combinations(candidate,2):
        visited_num += 1

        board[p1[0]][p1[1]] = board[p2[0]][p2[1]] = 1

        total = search_enemy(p1)
        total += search_enemy(p2)

        answer = max(answer, total)
        board[p1[0]][p1[1]] = board[p2[0]][p2[1]] = 0

    print(answer)

def search_enemy(p):
    sx,sy = p
    total = 0
    for d in range(4):
        nx = sx + dx[d]
        ny = sy + dy[d]

        if point_validator(nx,ny) and board[nx][ny] == 2 and visited[nx][ny] != visited_num:
            total += enemy_kill(nx,ny)

    return total
def enemy_kill(sx,sy):
    global visited

    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num

    cnt = 0
    while q:
        x,y = q.pop()
        cnt += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny):
                if board[nx][ny] == 0:
                    return 0
                if board[nx][ny] == 2 and visited[nx][ny] != visited_num:
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))
    return cnt


def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solv()
from sys import stdin
from itertools import combinations
from collections import deque

input = stdin.readline
dx = [0,-1,0]
dy = [-1,0,1]

n,m,d = map(int, input().split())

board = []
enemy_count = 0
for x in range(n):
    board.append(list(map(int, input().split())))
    enemy_count += board[x].count(1)

dead_map = [[0]*m for _ in range(n)]
dead_num = 0

visited = [[0]*m for _ in range(n)]
visited_num = 0

def solv():
    global dead_num
    answer = 0
    for archer in combinations(range(m),3):
        dead_count = 0
        dead_num += 1
        for h in range(n,0,-1):
            dead_count += attack(archer,h)


        answer = max(answer, dead_count)

    print(answer)

def attack(archer, x):
    global dead_map

    target = set()
    for y in archer:
        tx,ty = search_enemy(x,y)
        if tx != -1:
            target.add((tx,ty))

    for x,y in target:
        dead_map[x][y] = dead_num
    return len(target)
def search_enemy(sx,sy):
    global visited, visited_num
    visited_num += 1

    q = deque([(sx,sy,0)])

    while q:
        x,y,cnt = q.pop()

        if cnt == d:
            continue

        for dir in range(3):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx,ny,sx):
                if board[nx][ny] == 1 and dead_map[nx][ny] != dead_num:
                   return nx,ny

                visited[nx][ny] = visited_num
                q.appendleft((nx,ny,cnt+1))
    return -1,-1
def point_validator(x,y,sx):
    if x == sx:
        return False
    elif x < 0 or y < 0 or y >= m:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()
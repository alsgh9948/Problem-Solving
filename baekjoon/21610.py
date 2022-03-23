from sys import stdin
from collections import deque

input = stdin.readline
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]

clouds = deque([(n-2,0),(n-2,1),(n-1,0),(n-1,1)])
visited = [[0]*n for _ in range(n)]
visited_num = 0
def solv():
    global visited_num
    for d,s in commands:
        visited_num += 1

        targets = move_cloud(d-1,s)
        renew_board(targets)
        make_cloud()
    print_answer()
def print_answer():
    answer = 0
    for x in range(n):
        for y in range(n):
            answer += board[x][y]
    print(answer)
def move_cloud(d,s):
    global board,clouds,visited

    targets = []
    while clouds:
        x,y = clouds.pop()
        nx = (x + dx[d]*s)%n
        ny = (y + dy[d]*s)%n
        board[nx][ny] += 1

        if visited[nx][ny] != visited_num:
            visited[nx][ny] = visited_num
            targets.append((nx,ny))

    return targets

def renew_board(targets):
    for x,y in targets:
        for d in range(1,8,2):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                board[x][y] += 1

def make_cloud():
    for x in range(n):
        for y in range(n):
            if board[x][y] >= 2 and visited[x][y] != visited_num:
                clouds.appendleft((x,y))
                board[x][y] -= 2

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()
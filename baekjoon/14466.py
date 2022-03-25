from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,k,r = map(int, input().split())
board = [[0]*(n+1) for _ in range(n+1)]
road_board = [[[False]*4 for _ in range(n+1)] for _ in range(n+1)]

visited = [[0]*(n+1) for _ in range(n+1)]
visited_num = 0

for _ in range(r):
    x1,y1,x2,y2 = map(int, input().split())
    x = x2-x1
    y = y2-y1

    if (x,y) == (-1,0):
        d = 0
    elif (x,y) == (0,1):
        d = 1
    elif (x,y) == (1,0):
        d = 2
    else:
        d = 3
    road_board[x1][y1][d] = road_board[x2][y2][(d+2)%4] = True

cows = []
for _ in range(k):
    x,y = map(int, input().split())
    cows.append((x,y))
    board[x][y] = len(cows)

def solv():
    answer = 0
    for sx,sy in cows:
       answer += bfs(sx,sy)
    print(answer)

def bfs(sx,sy):
    global visited,visited_num
    visited_num += 1
    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num

    count = k-board[sx][sy]
    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,(d+2)%4):
                if board[sx][sy] < board[nx][ny]:
                    count -= 1
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny))
    return count
def point_validator(x,y,d):
    if x < 1 or y < 1 or x > n or y > n:
        return False
    elif road_board[x][y][d]:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()
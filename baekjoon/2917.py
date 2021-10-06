from sys import stdin
from collections import deque
import heapq

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = []
tree_q = deque()
tree_dist = [[-1]*m for _ in range(n)]
sx=sy=-1

for x in range(n):
    board.append(input().strip())
    for y in range(m):
        if board[x][y] == '+':
            tree_q.appendleft((x,y,0))
            tree_dist[x][y] = 0
        elif board[x][y] == 'V':
            sx,sy = x,y

def solv():
    set_tree_dist()
    print(dijkstra())

def dijkstra():
    answer = 9876543210
    pq = []
    visited = [[False]*m for _ in range(n)]

    heapq.heappush(pq,(-tree_dist[sx][sy],sx,sy))
    visited[sx][sy] = True

    while pq:
        cost,x,y = heapq.heappop(pq)

        answer = min(answer,-cost)

        if board[x][y] == 'J':
            return answer

        for d in range(4):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq,(-tree_dist[nx][ny],nx,ny))

def set_tree_dist():
    global tree_q, tree_dist

    while tree_q:
        x,y,t = tree_q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny) and tree_dist[nx][ny] == -1:
                tree_dist[nx][ny] = t+1
                tree_q.appendleft((nx,ny,t+1))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
solv()

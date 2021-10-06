from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 9876543210

def solv():
    problem_num = 1
    while True:
        n = int(input())
        if n == 0:
            return
        board = [list(map(int, input().split())) for _ in range(n)]
        dijkstra(n,board,problem_num)
        problem_num += 1

def dijkstra(n,board,problem_num):
    visited = [[False]*n for _ in range(n)]
    pq = [(board[0][0],0,0)]
    visited[0][0] = True
    while pq:
        cost,x,y = heappop(pq)

        if x == n-1 and y == n-1:
            print('Problem %d:% d' % (problem_num, cost))
            return
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,visited,n):
                visited[nx][ny] = True
                heappush(pq,(board[nx][ny] + cost,nx,ny))
def point_validator(x,y,visited,n):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return False
    return True

solv()
from sys import stdin
from collections import deque
import heapq

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,o = map(int, input().split())

board = [list(input().split()) for _ in range(n)]

tx,ty = map(int, input().split())
tx,ty = tx-1,ty-1

passenger = [()]
passenger_board = [[0]*n for _ in range(n)]

for idx in range(1,m+1):
    sx,sy,gx,gy = map(int, input().split())
    passenger_board[sx-1][sy-1] = idx
    passenger.append((gx-1,gy-1))

visited_num = 0

def solv():
    visited = [[0]*n for _ in range(n)]
    for _ in range(m):
        target = search_passenger(visited)
        if target == -1:
            return -1
        if not move_destination(target, visited):
            return -1
    return o

def search_passenger(visited):
    global tx,ty,o,visited_num,passenger_board
    visited_num += 1
    pq = []
    heapq.heappush(pq,(0,tx,ty))
    visited[tx][ty] = visited_num

    while pq:
        length,x,y = heapq.heappop(pq)

        if passenger_board[x][y] > 0:
            o -= length
            tx,ty = x,y
            target = passenger_board[x][y]
            passenger_board[x][y] = 0
            return target

        if o == length:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if point_validator(nx,ny,visited):
                visited[nx][ny] = visited_num
                heapq.heappush(pq,(length+1,nx,ny))
    return -1
def move_destination(target, visited):
    global visited_num,o,tx,ty,passenger_board
    visited_num += 1

    q = deque()
    q.appendleft((0,tx,ty))
    visited[tx][ty] = visited_num
    gx,gy = passenger[target]
    while q:
        length,x,y = q.pop()

        if x == gx and y == gy:
            o += length
            tx,ty = x,y
            return True

        if o == length:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, visited):
                visited[nx][ny] = visited_num
                q.appendleft((length+1,nx,ny))
    return False

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    elif board[x][y] == '1':
        return False
    return True

print(solv())
from sys import stdin
from collections import deque
from heapq import heappush, heappop

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,e = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
visited_num = 0

tx,ty = map(lambda x:int(x)-1, input().split())

p_num = 2
destination = [(),()]
for _ in range(m):
    x1,y1,x2,y2 = map(lambda x:int(x)-1, input().split())
    board[x1][y1] = p_num
    destination.append((x2,y2))
    p_num += 1

def solv():
    global board
    x,y = tx,ty
    remain_energy = e
    passenger_count = p_num-2
    while passenger_count > 0:
        x,y,used = search_passenger(x,y,remain_energy)
        if x == -1:
            print(-1)
            return
        remain_energy -= used
        target = destination[board[x][y]]
        board[x][y] = 0

        x,y,used = move_taxi(x,y,target,remain_energy)

        remain_energy += used
        passenger_count -= 1
    print(remain_energy)

def move_taxi(sx,sy,target,remain_energy):
    global visited, visited_num
    visited_num += 1

    q = deque([(sx,sy,0)])
    visited[sx][sy] = visited_num

    while q:
        x,y,cnt = q.pop()

        if (x,y) == target:
            return x,y,cnt

        if cnt == remain_energy:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                visited[nx][ny] = visited_num
                q.appendleft((nx,ny,cnt+1))
    return -1,-1,-1
def search_passenger(sx,sy,remain_energy):
    global visited,visited_num
    visited_num += 1
    visited[sx][sy] = visited_num

    pq = [(0,sx,sy)]

    while pq:
        cnt,x,y = heappop(pq)
        if cnt == remain_energy:
            return -1,-1,-1

        if board[x][y] > 1:
            return x, y, cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                visited[nx][ny] = visited_num
                heappush(pq,(cnt+1,nx,ny))
    return -1,-1,-1
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 1:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True
solv()
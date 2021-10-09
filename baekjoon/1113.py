from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = [list(map(int,input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited_num = 0
pools = [[]]

def solv():
    ans = 0
    check_pool()
    for pool in pools[1:]:
        height = pool[0]
        if height > 0:
            for x,y in pool[1:]:
                ans += height - board[x][y]
    print(ans)

def check_pool():
    pool_board = [[0]*m for _ in range(n)]

    for sx in range(n-1):
        for sy in range(m-1):
            if board[sx][sy] != 0 and pool_board[sx][sy] == 0:
                check_bfs(pool_board, sx, sy)
def check_bfs(pool_board,sx,sy):
    global pools,visited,visited_num
    visited_num += 1
    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num
    pool_points = [(sx,sy)]

    height = board[sx][sy]
    pool_height = 0

    while q:
        x,y = q.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if point_validator(nx,ny):
                if visited[nx][ny] == visited_num:
                    continue
                if board[nx][ny] > height:
                    if pool_height == 0:
                        pool_height = board[nx][ny]
                    else:
                        pool_height = min(board[nx][ny], pool_height)
                    continue

                visited[nx][ny] = visited_num
                q.appendleft((nx, ny))
                pool_points.append((nx,ny))
            else:
                return

    pool_num = len(pools)
    pools.append([pool_height])

    for x, y in pool_points:
        if pool_board[x][y] != 0:
            idx = pool_board[x][y]
            pools[idx][0] = 0
        pool_board[x][y] = pool_num
        pools[pool_num].append((x,y))

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()
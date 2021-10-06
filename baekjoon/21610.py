from sys import stdin
from collections import deque

input = stdin.readline
dx = [0, 0,-1,-1,-1,0,1,1, 1]
dy = [0,-1,-1, 0, 1,1,1,0,-1]

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

cloud_board = [[0]*n for _ in range(n)]
cloud_board_num = 0
def solv():
    global board,cloud_board,cloud_board_num
    for _ in range(m):
        cloud_board_num += 1
        d,s = map(int, input().split())

        water_copy_points = []
        while cloud:
            x, y = cloud.pop()

            nx = (x + dx[d] * (s % n)) % n
            ny = (y + dy[d] * (s % n)) % n

            board[nx][ny] += 1
            cloud_board[nx][ny] = cloud_board_num
            water_copy_points.append((nx, ny))

        for x, y in water_copy_points:
            for d in [2, 4, 6, 8]:
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx, ny):
                    board[x][y] += 1

        for x in range(n):
            for y in range(n):
                if board[x][y] >= 2 and cloud_board[x][y] != cloud_board_num:
                    cloud.append((x, y))
                    board[x][y] -= 2
    ans = 0
    for row in board:
        ans += sum(row)
    print(ans)

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 0:
        return False
    return True

solv()
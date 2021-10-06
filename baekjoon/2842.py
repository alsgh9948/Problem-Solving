from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

n = int(input())

board = []
sx=sy=-1
home_cnt = 0
for x in range(n):
    board.append(input().strip())
    for y in range(n):
        if board[x][y] == 'P':
            sx,sy=x,y
        elif board[x][y] == 'K':
            home_cnt += 1

stamina_board = []
stamina_list = set()
for x in range(n):
    stamina_board.append(list(map(int, input().split())))
    for num in stamina_board[x]:
        stamina_list.add(num)
stamina_list = sorted(list(stamina_list))

visited = [[0]*n for _ in range(n)]
visited_num = 0
def solv():
    low=high=0
    answer = 9876543210
    while low < len(stamina_list) and high < len(stamina_list):
        if bfs(stamina_list[low],stamina_list[high]):
            if low == high:
                print(0)
                return
            else:
                answer = min(answer,abs(stamina_list[low]-stamina_list[high]))
                low += 1
        else:
            high += 1
    print(answer)
def bfs(low,high):
    global visited,visited_num
    if stamina_board[sx][sy] < low or stamina_board[sx][sy] > high:
        return False

    visited_num += 1
    q = deque([(sx,sy)])
    visited[sx][sy] = visited_num

    cnt = 0
    while q:
        x,y = q.pop()

        if board[x][y] == 'K':
            cnt += 1

        if cnt == home_cnt:
            return True
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                if low <= stamina_board[nx][ny] <= high:
                    visited[nx][ny] = visited_num
                    q.appendleft((nx,ny))

    return False
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()
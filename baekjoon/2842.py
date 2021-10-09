from sys import stdin
from collections import deque
input = stdin.readline
dx = [-1,1,0,0,-1,1,-1, 1]
dy = [0,0,-1,1, 1,1,-1,-1]

n = int(input())
board = []
targets = []
visited = [[[0]]*n for _ in range(n)]
visited_num = 0

for x in range(n):
    board.append(input())
    for y in range(n):
        if board[x][y] != '.':
            targets.append((x,y))

height = [list(map(int, input().split())) for _ in range(n)]
ans_board = [[[] for _ in range(n)] for _ in range(n)]
def solv():
    set_min_max_height()
    ans = 987654321
    for x in range(n):
        for y in range(n):
            min_h,max_h,cnt = ans_board[x][y]
            if cnt == len(targets):
                ans = min(ans,max_h-min_h)
    print(ans)
def set_min_max_height():
    global visited,visited_num,ans_board
    for sx,sy in targets:
        flag = False
        visited_num += 1
        visited[sx][sy] = visited_num

        sh = height[sx][sy]
        q = deque([(sx,sy,sh,sh)])
        if not ans_board[sx][sy]:
            ans_board[sx][sy] = [sh,sh,1]
        while q:
            x,y,min_h,max_h = q.pop()
            if ans_board[x][y]:
                ans_board[x][y] = [min(ans_board[x][y][0], min_h),max(ans_board[x][y][1], max_h),ans_board[x][y][2]+1]
            else:
                ans_board[x][y] = [min_h,max_h,1]
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if point_validator(nx,ny):
                    nh = height[nx][ny]
                    visited[nx][ny] = visited_num
                    if board[nx][ny] == 'K':
                        q.appendleft((nx,ny,min(min_h,nh),max(max_h,nh)))
                    else:
                        q.appendleft((nx,ny,min(min_h,nh),max(max_h,nh)))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

solv()
from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())

board = [list(stdin.readline()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
def solv():
    ans = []
    for x in range(n):
        for y in range(m):
            if board[x][y] == '*':
                size = check_cross(x,y)
                if size > 0:
                    ans.append((x+1,y+1,size))

    if check_ans():
        print(len(ans))
        for row in ans:
            print(*row)
    else:
        print(-1)

def check_ans():
    for x in range(n):
        for y in range(m):
            if board[x][y] == '*' and not visited[x][y]:
                return False
    return True
def check_cross(sx,sy):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for size in range((min(n,m)//2),0,-1):
        q = deque()
        flag = True
        visited_list = [(sx, sy)]
        if sx - size < 0 or sy - size < 0 or sx + size >= n or sy + size >= m:
            continue
        if board[sx-size][sy] == '*' or board[sx][sy-size]  == '*' or board[sx+size][sy]  == '*' or board[sx][sy+size]  == '*':
            for d in range(4):
                nx = sx + dx[d]
                ny = sy + dy[d]
                if not point_validator(nx, ny):
                    flag = False
                    break

                q.appendleft((nx, ny, 1, d))
                visited_list.append((nx,ny))

            while q:
                x,y,cnt,d = q.pop()
                if cnt == size:
                    continue

                nx = x + dx[d]
                ny = y + dy[d]
                if not point_validator(nx, ny):
                    flag = False
                    break

                q.appendleft((nx,ny,cnt+1,d))
                visited_list.append((nx,ny))

            if flag:
                for x,y in visited_list:
                    global visited
                    visited[x][y] = True
                return size
    return 0
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '.':
        return False
    return True

solv()
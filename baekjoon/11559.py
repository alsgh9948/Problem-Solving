from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = [list(input()) for _ in range(12)]

def solv():
    ans = 0
    while True:
        visited = [[False]*6 for _ in range(12)]
        flag = False
        for x in range(11,-1,-1):
            for y in range(6):
                if board[x][y] != '.' and not visited[x][y]:
                    if check_block(x,y,visited):
                        flag = True
        if flag:
            drop_block()
            ans += 1
        else:
            return ans

def check_block(x,y,visited):
    cnt = 1
    burst_point = [(x,y)]
    q = deque()

    q.appendleft((x,y))
    visited[x][y] = True
    color = board[x][y]

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,color,visited):
                visited[nx][ny] = True

                q.appendleft((nx,ny))
                burst_point.append((nx,ny))
                cnt += 1

                if cnt >= 4:
                    return burst(burst_point,color)
    return False

def burst(burst_point,color):
    global board

    q = deque()
    for x,y in burst_point:
        board[x][y] = '.'
        q.appendleft((x,y))

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, color):
                board[nx][ny] = '.'
                q.appendleft((nx,ny))
    return True

def drop_block():
    global board
    for y in range(6):
        step = 0
        for x in range(11,-1,-1):
            if board[x][y] == '.':
                step += 1
            elif step > 0:
                board[x+step][y], board[x][y] = board[x][y], '.'

def point_validator(x,y,color,visited=None):
    if x < 0 or y < 0 or x >= 12 or y >= 6:
        return False
    elif visited and visited[x][y]:
        return False
    elif board[x][y] != color:
        return False
    return True

print(solv())
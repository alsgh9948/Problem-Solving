from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,l,r = map(int, input().strip().split())

board = [list(map(int, input().strip().split())) for _ in range(n)]

def solv():
    ans = 0
    while True:
        flag = False
        visited = [[False]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if not visited[x][y]:
                    movable,people_cnt = is_movable(x,y,visited)
                    if movable:
                        move_people(movable, people_cnt)
                        if not flag:
                            flag = True
                            ans += 1

        if not flag:
            return ans

def is_movable(sx,sy,visited):
    q = deque()
    q.appendleft((sx,sy))
    visited[sx][sy] = True
    people_cnt = board[sx][sy]
    movable = [(sx,sy)]

    while q:
        q_len = len(q)
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue

            sub = abs(board[x][y] - board[nx][ny])
            if l <= sub and sub <= r:
                visited[nx][ny] = True
                people_cnt += board[nx][ny]
                movable.append((nx,ny))
                q.appendleft((nx,ny))

    if len(movable) > 1:
        return movable,people_cnt
    else:
        return None, 0

def move_people(movable,people_cnt):
    global board
    new_people_cnt = people_cnt//len(movable)

    for x,y, in movable:
        board[x][y] = new_people_cnt
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return False
    return True

print(solv())
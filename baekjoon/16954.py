from collections import deque

dx = [0,-1,1,0,0,-1,1,-1,1]
dy = [0,0,0,-1,1,1,-1,-1,1]
board = []
wall_q = deque()
for i in range(8):
    board.append(list(input()))
    for j in range(8):
        if board[i][j] == '#':
            wall_q.append((i,j))

def solv():
    q = deque()
    t = 2
    visited = [[0]*8 for _ in range(8)]

    q.appendleft((7,0))
    visited[7][0] = 1
    while q:
        if not wall_q:
            return 1
        q_len = len(q)
        for _ in range(q_len):
            x,y = q.pop()

            if board[x][y] == '#':
                continue

            if x == 0 and y == 7:
                return 1

            for d in range(9):
                nx = x + dx[d]
                ny = y + dy[d]

                if not point_validator(nx,ny) or visited[nx][ny] == t:
                    continue

                visited[nx][ny] = t
                q.appendleft((nx,ny))
        dropdown_wall()
        t += 1
    return 0

def dropdown_wall():
    global board

    wall_q_len = len(wall_q)
    for _ in range(wall_q_len):
        x,y = wall_q.pop()
        board[x][y] = '.'
        x += 1
        if x < 8:
            wall_q.appendleft((x,y))
            board[x][y] = '#'
def point_validator(x,y,flag=True):
    if x < 0  or y < 0 or x >= 8 or y >= 8:
        return False
    elif flag and board[x][y] == '#':
        return False
    return True

print(solv())
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    global n
    n = len(board)
    return bfs(board)


def bfs(board):
    q = deque([(0, 0, 0, 1, 0, 0)])
    visited = [[[[False] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]

    visited[0][0][0][1] = 0

    while q:
        x1, y1, x2, y2, cnt, typ = q.pop()
        if x2 == y2 == n - 1:
            return cnt
        for d in range(4):
            nx1 = x1 + dx[d]
            ny1 = y1 + dy[d]

            nx2 = x2 + dx[d]
            ny2 = y2 + dy[d]

            if point_validator(nx1, ny1, nx2, ny2, board, visited):
                visited[nx1][ny1][nx2][ny2] = True
                q.appendleft((nx1, ny1, nx2, ny2, cnt + 1, typ))

        for r in range(4):
            nx1, ny1, nx2, ny2, nx3, ny3 = rotate_robot(x1, y1, x2, y2, typ, r)

            if rotate_validator(nx3,ny3,board) and point_validator(nx1, ny1, nx2, ny2, board, visited):
                visited[nx1][ny1][nx2][ny2] = True
                q.appendleft((nx1, ny1, nx2, ny2, cnt + 1, (typ+1)%2))

def rotate_robot(x1, y1, x2, y2, typ, r):
    if typ == 0:
        if r == 0:
            return x1, y1, x1 + 1, y1, x2 + 1, y2
        elif r == 1:
            return x1 - 1, y1, x1, y1, x2 - 1, y2
        elif r == 2:
            return x2, y2, x2 + 1, y2, x1 + 1, y1
        elif r == 3:
            return x2 - 1, y2, x2, y2, x1 - 1, y1
    elif typ == 1:
        if r == 0:
            return x1, y1 - 1, x1, y1, x2, y2 - 1
        elif r == 1:
            return x1, y1, x1, y1 + 1, x2, y2 + 1
        elif r == 2:
            return x2, y2 - 1, x2, y2, x1, y1 - 1
        elif r == 3:
            return x2, y2, x2, y2 + 1, x1, y1 + 1

def rotate_validator(x,y,board):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 1:
        return False
    return True

def point_validator(x1, y1, x2, y2, board, visited):
    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0 or x1 >= n or y1 >= n or x2 >= n or y2 >= n:
        return False
    elif board[x1][y1] == 1 or board[x2][y2] == 1:
        return False
    elif visited[x1][y1][x2][y2]:
        return False
    return True

a = [[0, 0, 0, 1, 1], [1, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
# a = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
print(solution(a))
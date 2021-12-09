from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

blocks = [
    [
        [[1, 0, 0], [1, 1, 1]],
        [[0, 1], [0, 1], [1, 1]]
    ],
    [
        [[1, 0], [1, 0], [1, 1]],
        [[0, 0, 1], [1, 1, 1]],
    ],
    [
        [[0, 1, 0], [1, 1, 1]],
    ]
]

def solution(input_board):
    global board, n, edges
    board = input_board
    n = len(board)
    edges = {}
    answer = 0

    set_squre_edge()

    while True:
        rst = search_target()
        if rst == -1:
            break
        answer += rst
    return answer

def search_target():
    for y in range(n):
        for x in range(n):
            if board[x][y] > 0:
                sx,sy = edges[board[x][y]]
                if select_block(sx, sy, board[x][y]):
                    return 1
                else:
                    break
    return -1

def set_squre_edge():
    global edges
    visited = [[False]*n for _ in range(n)]
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] != 0 and not visited[sx][sy]:
                edges[board[sx][sy]] = bfs(sx,sy,visited)

def bfs(sx,sy,visited):
    visited[sx][sy] = True
    q = deque([(sx, sy)])
    min_x, min_y = sx, sy
    typ = board[sx][sy]
    while q:
        x, y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if boundray_validator(nx,ny) and not visited[nx][ny] and board[nx][ny] == typ:
                min_x = min(min_x,nx)
                min_y = min(min_y,ny)
                visited[nx][ny] = True
                q.appendleft((nx,ny))
    return (min_x, min_y)

def select_block(sx, sy, typ):
    for i in range(3):
        for j in range(len(blocks[i])):
            block = blocks[i][j]
            if is_possible(sx, sy, block, typ):
                remove_block(sx, sy, block)
                return True
    return False


def remove_block(sx, sy, block):
    global board
    r, c = len(block), len(block[0])
    for x in range(sx, sx + r):
        for y in range(sy,sy + c):
            board[x][y] = 0


def is_possible(sx, sy, block, typ):
    r, c = len(block), len(block[0])
    for x in range(r):
        for y in range(c):
            tx, ty = sx + x, sy + y
            if boundray_validator(tx, ty):
                if (board[tx][ty] == typ and block[x][y] == 1):
                    continue
                elif (board[tx][ty] == 0 and block[x][y] == 0):
                    for nx in range(tx-1,-1,-1):
                        if board[nx][ty] != 0:
                            return False
                else:
                    return False
            else:
                return False


    return True


def boundray_validator(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

# a = [[0,0,0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0,0,0]
# ,[0,0,0,2,2,0,0,0,0,0]
# ,[0,0,0,2,1,0,0,0,0,0]
# ,[0,0,0,2,1,0,0,0,0,0]
# ,[0,0,0,0,1,1,0,0,0,0]
# ,[0,0,0,0,0,0,0,0,0,0]
# ,[0,0,0,0,0,0,0,0,0,0]]

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
print(solution(a))
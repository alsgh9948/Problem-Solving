def solution(input_n, build_frame):
    global board, n
    n = input_n
    answer = []

    board = [[-1] * (n + 1) for _ in range(n + 1)]

    for y, x, a, b in build_frame:
        if b == 0:
            remove_block(x, y, a)
        else:
            add_block(x, y, a)

    for x in range(n + 1):
        for y in range(n + 1):
            if board[x][y] == 2:
                answer.append([y, x, 0])
                answer.append([y, x, 1])
            elif board[x][y] != -1:
                answer.append([y, x, board[x][y]])

    answer.sort()
    return answer

def remove_block(x, y, typ):
    global board
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]

    tmp = board[x][y]
    if board[x][y] == 2:
        if typ == 0:
            board[x][y] = 1
        else:
            board[x][y] = 0
    else:
        board[x][y] = -1
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx <= n and 0 <= ny <= n and board[nx][ny] != -1:
            if not is_possible(nx,ny,board[nx][ny],False):
                board[x][y] = tmp
                return

def add_block(x, y, typ):
    global board
    if is_possible(x, y, typ):
        if board[x][y] == -1:
            board[x][y] = typ


def is_possible(x, y, typ, flag=True):
    if typ == 0:
        if x == 0:
            return True
        elif board[x][y] == 1 and flag:
            board[x][y] = 2
            return True
        elif board[x - 1][y] == 0:
            return True
        elif y > 0 and board[x][y-1] in [1,2]:
            return True
    else:
        if x > 0:
            if board[x-1][y] == 0:
                if board[x][y] == 0 and flag:
                    board[x][y] = 2
                return True
            elif y < n and board[x-1][y+1] == 0:
                return True

        if 0 < y < n and board[x][y-1] in [1,2] and board[x][y+1] in [1,2]:
            return True
    return False

a = 5
b = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
# b =  [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [2, 2, 0, 1], [2,1,0,1],[3,1,0,0]]
print(solution(a,b))
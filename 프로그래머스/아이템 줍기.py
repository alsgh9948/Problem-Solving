dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    global board, in_out_board, visited, answer
    answer = 9876543210
    in_out_board = [[[0] * 4 for _ in range(105)] for _ in range(105)]
    board = [[0] * 105 for _ in range(105)]
    visited = [[False]*105 for _ in range(105)]

    set_board(rectangle)

    visited[characterY*2][characterX*2] = True
    for d in range(4):
        nx = characterY*2 + dx[d]
        ny = characterX*2 + dy[d]
        if board[nx][ny] > 0 and -1 not in in_out_board[nx][ny]:
            dfs(nx, ny, 1, itemY*2, itemX*2)
    return answer


def dfs(x, y, cnt, tx, ty):
    global answer,visited
    if (x, y) == (tx, ty):
        answer = min(cnt//2, answer)
        visited[tx][ty] = False
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if board[nx][ny] > 0 and -1 not in in_out_board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, tx, ty)

def set_board(rectangle):
    global board, in_out_board
    num = 0
    for sy, sx, ey, ex in rectangle:
        for x in range(sx*2, ex*2+1):
            for y in range(sy*2, ey*2+1):
                board[x][y] += 1
                if x in (sx*2, ex*2) or y in (sy*2, ey*2):
                    in_out_board[x][y][num] = 1
                else:
                    in_out_board[x][y][num] = -1
        num += 1
def solution(n, build_frame):
    global board
    n += 1
    board = [[[[], []] for _ in range(n)] for _ in range(n)]

    for x, y, a, b in build_frame:
        if b == 0:
            tmp = board[x][y][a]
            board[x][y][a] = []
            dd = [
                [(-1,1,1),(0,1,0),(0,1,1),(1,1,1)],
                [(-1,0,1),(0,0,0),(1,0,0),(1,0,1)]
            ]
            for d in dd[a]:
                nx = x + d[0]
                ny = y + d[1]
                if (board[nx][ny][d[2]] and not is_possible(nx,ny,d[2],n)):
                    board[x][y][a] = tmp
                    break
        elif b == 1:
            if is_possible(x, y, a, n):
                board[x][y][a] = [x, y, a]

    answer = []
    for x in range(n):
        for y in range(n):
            if board[x][y][0]:
                answer.append(board[x][y][0])

            if board[x][y][1]:
                answer.append(board[x][y][1])

    answer.sort()
    return answer

def is_possible(x, y, a, n):
    if a == 0:
        if y == 0:
            return True
        elif board[x][y-1][0]:
            return True
        elif (x > 0 and board[x-1][y][1]) or board[x][y][1]:
            return True
        else:
            return False
    else:
        if (y > 0 and board[x][y-1][0]) or (x < n and y > 0 and board[x+1][y - 1][0]):
            return True
        elif x > 0 and x+1 < n and board[x-1][y][1] and board[x+1][y][1]:
            return True
        else:
            return False
a = 5
# b = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
b = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(a,b))
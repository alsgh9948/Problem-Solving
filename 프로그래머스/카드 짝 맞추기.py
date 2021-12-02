# from heapq import heappush, heappop
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def solution(board, r, c):
#     global answer
#     answer = 9876543210
#     board, max_num = renew_board(board)
#     visited = [[[9876543210]*(2 ** max_num) for _ in range(4)] for _ in range(4)]
#     bfs(board, r, c, visited, max_num)
#     return answer
#
#
# def bfs(board, sx, sy, visited, max_num):
#     global answer
#     pq = []
#
#     if board[sx][sy] > 0:
#         num = board[sx][sy]
#         nxt_visited_bit = (1 << num)
#         nxt = num - 1 if num % 2 == 0 else num + 1
#         pq.append((2, sx, sy, nxt_visited_bit, nxt))
#         visited[sx][sy][nxt_visited_bit] = 2
#     else:
#         visited[sx][sy][0] = 1
#         pq.append((1,sx,sy, 0, -1))
#     while pq:
#         count, x, y, visited_bit, target = heappop(pq)
#         if visited_bit == (2**max_num)-2:
#             answer = min(answer, count-1)
#             continue
#         for d in range(4):
#             nx, ny = x, y
#             for typ in range(2):
#                 if typ == 0:
#                     nx += dx[d]
#                     ny += dy[d]
#                 else:
#                     nx,ny = ctrl_move(nx, ny, d, board, visited_bit)
#
#                 if point_validator(nx, ny, visited, visited_bit, count):
#                     visited[nx][ny][visited_bit] = count
#                     num = board[nx][ny]
#                     if board[nx][ny] > 0 and visited_bit & (1<<num) == 0:
#                         nxt_visited_bit = visited_bit | (1 << num)
#                         if target == -1:
#                             nxt = num - 1 if num % 2 == 0 else num + 1
#                             heappush(pq,(count + 2, nx, ny, nxt_visited_bit, nxt))
#                         elif target == num:
#                             heappush(pq,(count + 2, nx, ny, nxt_visited_bit, -1))
#                         else:
#                             heappush(pq,(count + 1, nx, ny, visited_bit, target))
#                         break
#                     else:
#                         heappush(pq, (count + 1, nx, ny, visited_bit, target))
#                 else:
#                     break
#
# def ctrl_move(x,y,d,board,visited_bit):
#     for _ in range(2):
#         x += dx[d]
#         y += dy[d]
#         if boundray_validator(x, y):
#             num = board[x][y]
#             if board[x][y] > 0 and visited_bit & (1 << num) == 0:
#                 break
#         else:
#             x -= dx[d]
#             y -= dy[d]
#             break
#     return x,y
#
# def boundray_validator(x, y):
#     if x < 0 or y < 0 or x >= 4 or y >= 4:
#         return False
#     return True
#
# def point_validator(x, y, visited, visited_bit, count):
#     if not boundray_validator(x, y):
#         return False
#     elif visited[x][y][visited_bit] < count:
#         return False
#     return True
#
# def renew_board(board):
#     pairs = [[] for _ in range(7)]
#
#     for x in range(4):
#         for y in range(4):
#             if board[x][y] > 0:
#                 pairs[board[x][y]].append((x,y))
#
#     new_num = 1
#     for pair in pairs:
#         for x, y in pair:
#             board[x][y] = new_num
#             new_num += 1
#     return board, new_num
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board, r, c):
    global answer
    answer = 9876543210
    board, max_num = renew_board(board)
    visited = [[[[False]*(2 ** max_num) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    bfs(board, r, c, visited, max_num)
    return answer


def bfs(board, sx, sy, visited, max_num):
    global answer
    q = deque()

    if board[sx][sy] > 0:
        num = board[sx][sy]
        nxt_visited_bit = (1 << num)
        nxt = num - 1 if num % 2 == 0 else num + 1
        q.appendleft((sx, sy, 1, nxt_visited_bit, nxt))
    q.appendleft((sx,sy, 0, 0, -1))
    while q:
        x, y, count, visited_bit, target = q.pop()

        if visited_bit == (2**max_num)-2:
            answer = min(answer, count)
            continue
        for d in range(4):
            nx, ny = x, y
            for typ in range(2):
                if typ == 0:
                    nx += dx[d]
                    ny += dy[d]
                else:
                    nx,ny = ctrl_move(nx, ny, d, board, visited_bit)

                if point_validator(nx, ny, visited, visited_bit,d):
                    visited[nx][ny][d][visited_bit] = True
                    num = board[nx][ny]
                    if board[nx][ny] > 0 and visited_bit & (1<<num) == 0:
                        nxt_visited_bit = visited_bit | (1 << num)
                        if target == -1:
                            nxt = num - 1 if num % 2 == 0 else num + 1
                            q.appendleft((nx, ny, count + 2, nxt_visited_bit, nxt))
                        elif target == num:
                            q.appendleft((nx, ny, count + 2, nxt_visited_bit, -1))
                        else:
                            q.appendleft((nx, ny, count + 1, visited_bit, target))
                        break
                    else:
                        q.appendleft((nx, ny, count + 1, visited_bit, target))
                else:
                    break

def ctrl_move(x,y,d,board,visited_bit):
    for _ in range(2):
        x += dx[d]
        y += dy[d]
        if boundray_validator(x, y):
            num = board[x][y]
            if board[x][y] > 0 and visited_bit & (1 << num) == 0:
                break
        else:
            x -= dx[d]
            y -= dy[d]
            break
    return x,y
def boundray_validator(x, y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True


def point_validator(x, y, visited, visited_bit,d):
    if not boundray_validator(x, y):
        return False
    elif visited[x][y][d][visited_bit]:
        return False
    return True


def renew_board(board):
    pairs = [[] for _ in range(7)]

    for x in range(4):
        for y in range(4):
            if board[x][y] > 0:
                pairs[board[x][y]].append((x, y))

    new_num = 1
    for pair in pairs:
        for x, y in pair:
            board[x][y] = new_num
            new_num += 1
    return board, new_num

a = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
b = 1
c = 0
print(solution(a,b,c))


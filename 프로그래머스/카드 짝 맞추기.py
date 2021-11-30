from collections import deque
from itertools import permutations

INF = 9876543210
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board, r, c):
    global n, locations, cost, answer
    answer = INF
    n = 4
    cost = set_cost(board)

    locations, targets = set_target(board)

    for order in permutations(targets, len(targets)):
        simul(order, 0, r, c, 0)
    return answer


def simul(order, idx, x, y, count):
    global answer
    if idx == len(order):
        answer = min(answer, count)
        return
    now = x * 4 + y

    nx1, ny1 = locations[order[idx]][0]
    nx2, ny2 = locations[order[idx]][1]

    nxt1 = nx1 * 4 + ny1
    nxt2 = nx2 * 4 + ny2

    nxt_count = count + cost[now][nxt1] + cost[nxt1][nxt2]+2
    simul(order, idx + 1, nx2, ny2, nxt_count)

    nxt_count = count + cost[now][nxt2] + cost[nxt1][nxt2]+2
    simul(order, idx + 1, nx1, ny1, nxt_count)


def set_target(board):
    locations = [[] for _ in range(7)]
    targets = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                num = board[x][y]
                if not locations[num]:
                    targets.append(num)
                locations[num].append((x, y))
    return locations, targets


def set_cost(board):
    cost = [[INF]*16 for _ in range(16)]

    for start in range(16):
        q = deque([(start // 4, start % 4, 0)])
        cost[start][start] = 0

        while q:
            x, y, c = q.pop()
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                tmp = []
                if point_validator(nx,ny):
                    tmp.append((nx,ny))
                    if board[nx][ny] == 0:
                        for _ in range(3):
                            nx += dx[d]
                            ny += dy[d]

                            if point_validator(nx, ny):
                                if board[nx][ny] != 0:
                                    tmp.append((nx,ny))
                                    break
                            else:
                                nx -= dx[d]
                                ny -= dy[d]
                                break
                for nx,ny in tmp:
                    dest = nx * 4 + ny
                    if cost[start][dest] > c + 1:
                        cost[start][dest] = c + 1
                        q.appendleft((nx, ny, c + 1))
    return cost

def point_validator(x, y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True

a = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
b = 1
c = 0
print(solution(a,b,c))
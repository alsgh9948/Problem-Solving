INF = 9876543210

def solution(n, s, a, b, fares):
    cost_board = [[INF] * (n + 1) for _ in range(n + 1)]

    for x, y, cost in fares:
        cost_board[x][y] = cost
        cost_board[y][x] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    cost_board[i][j] = 0
                elif cost_board[i][j] > cost_board[i][k] + cost_board[k][j]:
                    cost_board[i][j] = cost_board[i][k] + cost_board[k][j]

    answer = INF
    for start in range(1,n+1):
        answer = min(answer, cost_board[start][s]+cost_board[start][a]+cost_board[start][b])
    return answer

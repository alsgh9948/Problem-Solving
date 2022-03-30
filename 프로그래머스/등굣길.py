def solution(m, n, puddles):
    count = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if [y - 1, x - 1] in puddles:
                continue

            if x == 0 and y == 0:
                continue
            elif x == 0 or y == 0:
                count[x][y] = 1
            else:
                count[x][y] = count[x][y - 1] + count[x - 1][y]
    return count[n - 1][m - 1] % 1000000007

a = 4
b = 3
c = [[2, 2]]
print(solution(a,b,c))
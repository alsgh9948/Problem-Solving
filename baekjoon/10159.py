from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

adj_mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adj_mat[a][b] = 1
    adj_mat[b][a] = -1

def solv():
    global adj_mat
    for k in range(1,n+1):
        for i in range(1,n+1):
            if k == i:
                continue
            for j in range(1,n+1):
                if i == j:
                    adj_mat[i][j] = 2
                elif adj_mat[i][j] == 0 and adj_mat[i][k] == adj_mat[k][j] != 0:
                    adj_mat[i][j] = adj_mat[i][k]
    for row in adj_mat[1:]:
        print(row.count(0)-1)
solv()
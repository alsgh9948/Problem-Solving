from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
INF = 9876543210
adj_mat = [[[INF,INF] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    adj_mat[a][b] = [b,c]
    adj_mat[b][a] = [a,c]

def solv():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    adj_mat[i][j][0] = -1
                else:
                    if adj_mat[i][j][1] > adj_mat[i][k][1] + adj_mat[k][j][1]:
                        adj_mat[i][j] =[adj_mat[i][k][0], adj_mat[i][k][1] + adj_mat[k][j][1]]

    for row in adj_mat[1:]:
        for before,cost in row[1:]:
            if before == -1:
                print('-',end=' ')
            else:
                print(before,end=' ')
        print()

solv()
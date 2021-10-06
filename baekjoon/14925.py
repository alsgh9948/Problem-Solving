from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
board = ([['0']*(m+1)])+[['0']+list(input().split()) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

def solv():
    ans = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            if board[x][y] == '0':
                dp[x][y] = min(dp[x-1][y-1], min(dp[x][y-1],dp[x-1][y]))+1
                ans = max(ans,dp[x][y])
    print(ans)

solv()
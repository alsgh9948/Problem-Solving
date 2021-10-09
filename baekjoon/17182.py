n,k = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]

answer = 9876543210
visited = [False]*n
visited[k] = True
def solv():
    global cost,visited

    for l in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif cost[i][j] > cost[i][l] + cost[l][j]:
                    cost[i][j] = cost[i][l] + cost[l][j]

    dfs(1,k,0)
    print(answer)
def dfs(cnt, now, total):
    global answer,visited
    if cnt == n:
        answer = min(total,answer)
        return

    for nxt in range(n):
        if now == nxt or visited[nxt]:
            continue
        visited[nxt] = True
        dfs(cnt+1,nxt,total+cost[now][nxt])
        visited[nxt] = False

solv()
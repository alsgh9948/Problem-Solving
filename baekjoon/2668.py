from sys import stdin

input = stdin.readline

n = int(input())
graph = [0]*(n+1)

for idx in range(1,n+1):
    graph[idx] = int(input())

def solv():
    visited = [0]*(n+1)
    ans_cnt = 0
    ans_arr = []
    for start in range(1,n+1):
        if visited[start] == 0:
            visited[start] = dfs(start,graph[start],visited)

    for num in range(1,n+1):
        status = visited[num]
        if status == 1:
            ans_cnt += 1
            ans_arr.append(num)

    print(ans_cnt)
    for num in ans_arr:
        print(num)
def dfs(start,now,visited):
    if start == now:
        return 1
    elif visited[now] in [-1,1]:
        return 0

    nxt = graph[now]
    visited[now] = -1
    visited[now] = dfs(start,nxt,visited)
    return visited[now]

solv()
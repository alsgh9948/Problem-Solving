from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

input = stdin.readline

n = int(input())

tree = [[-1,-1,[]] for _ in range(n+1)]
include_child = [False]*(n+1)

for _ in range(n-1):
    parent,child,cost = map(int, input().split())

    tree[parent][2].append(child)
    tree[child][0] = parent
    tree[child][1] = cost

    include_child[parent] = True

answer = 0
def solv():
    visited = [False]*(n+1)
    dist = [[-1,-1] for _ in range((n+1))]
    for start in range(1,n+1):
        if not include_child[start]:
            dist[start] = [0,0]
            visited[start] = True
            dfs(start,0,visited,dist)
            visited[start] = False
    print(answer)

def dfs(now,cost,visited,dist):
    global answer

    flag = False
    parent = tree[now][0]
    if parent != -1:
        if not visited[parent] and dist[parent][0] < cost+tree[now][1]:
            dist[parent][0] = cost+tree[now][1]
            visited[parent] = True
            dfs(parent,cost+tree[now][1],visited,dist)
            visited[parent] = False
            flag = True

    if tree[now][2]:
        for child in tree[now][2]:
            if not visited[child] and dist[child][1] < cost+tree[child][1]:
                dist[child][1] = cost+tree[child][1]
                visited[child] = True
                dfs(child,cost + tree[child][1],visited,dist)
                visited[child] = False
                flag = True

    if not flag:
        answer = max(answer, cost)

solv()
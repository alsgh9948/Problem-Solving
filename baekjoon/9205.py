from sys import stdin

input = stdin.readline

tc = int(input())

def solv():
    global n,conv,end
    n = int(input())
    start = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))

    end = list(map(int, input().split()))

    if calc_dist(start,end) <= 1000:
        return 'happy'
    else:
        visited = [False]*n
        for idx in range(n):
            if not visited[idx]:
                if calc_dist(start,conv[idx]) <= 1000:
                    visited[idx] = True
                    if dfs(idx,visited):
                        return 'happy'

    return 'sad'

def dfs(now,visited):
    if calc_dist(conv[now],end) <= 1000:
        return True
    for nxt in range(n):
        if not visited[nxt]:
            if calc_dist(conv[now],conv[nxt]) <= 1000:
                visited[nxt] = True
                if dfs(nxt,visited):
                    return True
    return False

def calc_dist(start,end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

for _ in range(tc):
    print(solv())
from sys import stdin

input = stdin.readline

n = int(input())
board = list(map(int, input().split()))
start = int(input())-1
visited = [0]*n

def solv():
    print(dfs(start))

def dfs(now):
    global visited
    visited[now] = True

    count = 1
    left = now-board[now]
    right = now+board[now]

    if left >= 0 and not visited[left]:
        count += dfs(left)

    if right < n and not visited[right]:
        count += dfs(right)

    return count

solv()
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
m = int(input())

board = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

def solv():
    global board

    q = deque([1])
    answer = 0

    visited = [False]*(n+1)

    visited[1] = True

    while q:
        now = q.pop()

        for nxt in board[now]:
            if not visited[nxt]:
                answer += 1
                visited[nxt] = True
                q.appendleft(nxt)

    print(answer)

solv()
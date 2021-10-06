from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
board = list(map(int, input().split()))

def solv():
    q = deque([(0,0)])
    visited = [False]*n
    visited[0] = True

    while q:
        now,cnt = q.pop()
        if now == n-1:
            print(cnt)
            return

        step = board[now]
        nxt = now
        for _ in range(step):
            nxt += 1
            if nxt < n and not visited[nxt]:
                visited[nxt] = True
                q.appendleft((nxt,cnt+1))
    print(-1)

solv()
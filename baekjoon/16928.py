from collections import deque

n, m = map(int, input().strip().split())

board = [0] * 101

for _ in range(n+m):
    a,b = map(int, input().strip().split())
    board[a] = b

def solv():
    visited = [False] * 101
    q = deque()

    q.appendleft((1,0))
    visited[1] = True

    while q:
        now, cnt = q.pop()
        if now == 100:
            return cnt
        for i in range(1,7):
            nxt = now + i
            if nxt > 100:
                break

            if visited[nxt]:
                continue

            visited[nxt] = True
            if board[nxt] != 0:
                nxt = board[nxt]
                if visited[nxt]:
                    continue
                visited[nxt] = True
            q.appendleft((nxt,cnt+1))

print(solv())
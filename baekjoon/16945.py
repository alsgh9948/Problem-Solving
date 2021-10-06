from collections import deque

a,b = map(int, input().strip().split())

def bfs():
    q = deque()

    q.appendleft((a,1))
    while q:
        now,cnt = q.pop()

        if now == b:
            return cnt

        if now*2 <= b:
            q.appendleft((now*2,cnt+1))

        if now*10+1 <= b:
            q.appendleft((now*10+1,cnt+1))

    return -1

print(bfs())

from collections import deque

f,s,g,u,d = map(int,input().strip().split())

def bfs():
    visited = [False] * (f + 1)
    q = deque()

    q.appendleft((s,0))
    visited[s] = True

    while q:
        now,cnt = q.pop()

        if now == g:
            return cnt

        nxt = now + u
        if point_validator(nxt,visited):
            visited[nxt] = True
            q.appendleft((nxt,cnt+1))

        nxt = now - d
        if point_validator(nxt,visited):
            visited[nxt] = True
            q.appendleft((nxt,cnt+1))

    return -1

def point_validator(nxt,visited):
    if nxt < 1 or nxt > f:
        return False
    elif visited[nxt]:
        return False
    return True

ans = bfs()
print("use the stairs" if ans == -1 else ans)
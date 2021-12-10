from collections import deque

a,b,n,m = map(int,input().split())
def solv():
    global a,b
    visited = [False]*(100001)
    visited[n] = True
    q = deque([(n,0)])

    while q:
        now,cnt = q.pop()

        if now == m:
            print(cnt)
            return

        for nxt in [now+1,now-1,now+a,now-a,now+b,now-b,now*a,now*b]:
            if 0 <= nxt < 100001 and not visited[nxt]:
                visited[nxt] = True
                q.appendleft((nxt,cnt+1))

solv()
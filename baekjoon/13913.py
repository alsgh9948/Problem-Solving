from collections import deque

n,k = map(int, input().split())

def bfs():
    visited = [-2]*100001

    q = deque()
    q.appendleft(n)
    visited[n] = -1
    while q:
        now= q.pop()
        if now == k:
            ans = deque()
            ans.appendleft(k)
            cur = k
            while visited[cur] != -1:
                ans.appendleft(visited[cur])
                cur = visited[cur]
            print(len(ans)-1)
            print(*ans)
            return

        if now + 1 <= 100000 and visited[now + 1] == -2:
            visited[now + 1] = now
            q.appendleft(now+1)

        if now - 1 >= 0 and visited[now - 1] == -2:
            visited[now - 1] = now
            q.appendleft(now-1)

        if now*2 >= 0 and now*2 <= 100000 and visited[now * 2] == -2:
            visited[now * 2] = now
            q.appendleft(now*2)

bfs()
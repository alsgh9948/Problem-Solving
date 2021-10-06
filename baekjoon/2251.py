from collections import deque

A,B,C = map(int,input().strip().split())

def bfs():
    ans = []
    visited = [[False]*(B+1) for _ in range(A+1)]

    q = deque()
    q.appendleft((0,0,C))
    while q:
        a,b,c = q.pop()

        if visited[a][b]: continue

        if a == 0:
            ans.append(c)

        visited[a][b] = True
        if a+b <= B:
            q.appendleft((0,a+b,c))
        else:
            q.appendleft((a+b-B,B,c))

        if a+c <= C:
            q.appendleft((0,b,a+c))
        else:
            q.appendleft((a+c-C,b,C))

        if b+a <= A:
            q.appendleft((b+a,0,c))
        else:
            q.appendleft((A,b+a-A,c))

        if b+c <= C:
            q.appendleft((a,0,b+c))
        else:
            q.appendleft((a,b+c-C,C))

        if c+a <= A:
            q.appendleft((c+a,b,0))
        else:
            q.appendleft((A,b,c+a-A))

        if c+b <= B:
            q.appendleft((a,c+b,0))
        else:
            q.appendleft((a,B,c+b-B))

    ans.sort()
    print(*ans)

bfs()




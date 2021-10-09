from collections import deque

a,b,c = map(int, input().strip().split())
d = a+b+c
def bfs():
    visited = [[False]*(1501) for _ in range(1501)]
    q = deque()

    q.appendleft((a,b))
    visited[a][b] = True

    while q:
        x,y = q.pop()
        z = d-(x+y)
        if x == y == z:
            return 1

        if x != y:
            if x > y:
                if not visited[x-y][y+y]:
                    q.appendleft((x-y,y+y))
                    visited[x-y][y+y] = True
            else:
                if not visited[x+x][y-x]:
                    q.appendleft((x+x,y-x))
                    visited[x+x][y-x] = True
        if x != z:
            if x > z:
                if not visited[x-z][y]:
                    q.appendleft((x-z,y))
                    visited[x-z][y] = True
            else:
                if not visited[x+x][y]:
                    q.appendleft((x+x,y))
                    visited[x+x][y] = True

        if y != z:
            if y > z:
                if not visited[x][y-z]:
                    q.appendleft((x,y-z))
                    visited[x][y-z] = True
            else:
                if not visited[x][y+y]:
                    q.appendleft((x,y+y))
                    visited[x][y+y] = True

    return 0

print(bfs())
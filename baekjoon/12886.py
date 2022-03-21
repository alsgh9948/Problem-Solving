from collections import deque

a,b,c = map(int, input().split())

def solv():
    total = a+b+c
    visited = [[False]*2001 for _ in range(2001)]
    q = deque([(a,b)])
    visited[a][b] = True

    while q:
        x,y = q.pop()
        z = total-x-y
        if x == y == z:
            print(1)
            return

        if x != y:
            if x < y:
                nx,ny = x+x,y-x
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
            else:
                nx,ny = y+y,x-y
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
        if x != z:
            if x < z:
                nx,ny = x+x,y
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
            else:
                nx,ny = x-z,y
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
        if y != z:
            if y < z:
                nx,ny = x,y+y
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
            else:
                nx,ny = x,y-z
                if not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True

    print(0)

solv()
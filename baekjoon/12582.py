from collections import deque

n = int(input())

def solv():
    visited = [0]*(n+1)

    q = deque([n])
    visited[n] = -1

    while q:
        now = q.pop()

        if now == 0:
            continue
        if now == 1:
            break
        if now%3 == 0 and visited[now//3] == 0:
            visited[now//3] = now
            q.appendleft(now//3)

        if now%2 == 0 and visited[now//2] == 0:
            visited[now//2] = now
            q.appendleft(now//2)

        if visited[now-1] == 0:
            visited[now-1] = now
            q.appendleft(now-1)


    nums = [1]
    nxt = visited[1]
    while nxt != -1:
        nums.append(nxt)
        nxt = visited[nxt]

    print(len(nums)-1)
    print(*nums[::-1])

solv()
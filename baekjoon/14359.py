from collections import deque

s,t = map(int,input().strip().split())

def bfs():
    q = deque()
    visited = set()

    q.appendleft((s,[]))

    while q:
        now,op = q.pop()

        if now == t:
            return ''.join(op)

        if now*now <= t and not now*now in visited:
            visited.add(now*now)
            q.appendleft((now*now,op+['*']))

        if now*2 <= t and not now*2 in visited:
            visited.add(now*2)
            q.appendleft((now*2,op+['+']))

        if not 0 in visited:
            visited.add(0)
            q.appendleft((0,op+['-']))

        if now != 0 and not 1 in visited:
            visited.add(1)
            q.appendleft((1,op+['/']))
    return -1
if s == t:
    print(0)
else:
    print(bfs())
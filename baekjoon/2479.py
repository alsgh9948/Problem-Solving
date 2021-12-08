from sys import stdin
from collections import deque
input = stdin.readline

n,k = map(int, input().split())
bits = [input().strip() for _ in range(n)]
sn,en = map(lambda x:int(x)-1, input().split())

def solv():
    visited = [-1]*n
    candidate = set_candidate()

    q = deque([(sn,0)])
    visited[sn] = sn

    while q:
        now,cnt = q.pop()
        if now == en:
            print_answer(visited)
            return

        for nxt in candidate[now]:
            if visited[nxt] == -1:
                visited[nxt] = now
                q.appendleft((nxt,cnt))
    print(-1)
def print_answer(visited):
    path = [en+1]
    nxt = visited[en]
    while visited[nxt] != nxt:
        path.append(nxt+1)
        nxt = visited[nxt]

    path.append(sn+1)
    path.reverse()
    print(*path)
def set_candidate():
    candidate = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            flag = False
            for a,b in zip(bits[i],bits[j]):
                if a != b:
                    if flag:
                        break
                    flag = True
            else:
                candidate[i].append(j)
                candidate[j].append(i)
    return candidate

solv()
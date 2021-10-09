from sys import stdin
from collections import deque

n,k = map(int,stdin.readline().strip().split())

ladder = []

for _ in range(2):
    ladder.append(list(stdin.readline().strip()))

def bfs():
    visited = [[False]*n for _ in range(2)]
    q = deque()
    tail = 0

    visited[0][0] = True
    q.appendleft((0,0))

    while q:
        q_len = len(q)
        for _ in range(q_len):
            ladder_num, now = q.pop()
            nxt = now+1
            if nxt >= n:
                return 1
            elif point_validator(nxt,ladder_num,visited):
                q.appendleft((ladder_num,nxt))
                visited[ladder_num][nxt] = True

            nxt = now-1
            if nxt > tail and point_validator(nxt,ladder_num,visited):
                q.appendleft((ladder_num,nxt))
                visited[ladder_num][nxt] = True

            nxt = now+k
            nxt_ladder = (ladder_num+1)%2
            if nxt >= n:
                return 1
            elif point_validator(nxt,nxt_ladder,visited):
                q.appendleft((nxt_ladder,nxt))
                visited[nxt_ladder][nxt] = True
        tail += 1
    return 0
def point_validator(nxt,ladder_num,visited):
    if visited[ladder_num][nxt]:
        return False
    elif ladder[ladder_num][nxt] == '0':
        return False
    return True

print(bfs())
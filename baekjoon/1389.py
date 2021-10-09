from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())

adj_mat = [[False]*n for _ in range(n)]
visited = [0]*n
visited_num = 0
for _ in range(m):
    a,b = map(int, input().split())
    adj_mat[a-1][b-1]=adj_mat[b-1][a-1]=True

def solv():
    global visited_num
    answer = (9876543210,n)

    for start in range(n):
        visited_num += 1
        answer = min(answer, (bfs(start),start))
    print(answer[1]+1)
def bfs(start):
    global visited
    tmp = 0

    q = deque([(start,0)])
    visited[start] = visited_num

    while q:
        now,cnt = q.pop()

        for nxt in range(n):
            if adj_mat[now][nxt] and visited[nxt] != visited_num:
                tmp += cnt+1
                visited[nxt] = visited_num
                q.appendleft((nxt,cnt+1))
    return tmp

solv()

import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n = int(sys.stdin.readline())

_map = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]

cnt_list = []
def bfs(x,y,num):
    global _map
    q = deque()
    q.append((x,y))
    group_cnt = 0

    while q:
        x,y = q.pop()
        _map[x][y] = num
        group_cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= n or ny >=n) or _map[nx][ny] != 1:
                continue
            _map[nx][ny] = num
            q.appendleft((nx,ny))
    cnt_list.append(group_cnt)

def dfs(x,y,num):
    global _map
    tmp_cnt = 1
    _map[x][y] = num
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or ny < 0 or nx >= n or ny >= n) or _map[nx][ny] != 1:
            continue
        tmp_cnt += dfs(nx,ny,num)
    return tmp_cnt

num = -1
for i in range(n):
    for j in range(n):
        if _map[i][j] == 1:
            # bfs(i,j,num)

            cnt_list.append(dfs(i,j,num))
            num -= 1

cnt_list.sort()
print(len(cnt_list))
for ans_cnt in cnt_list:
    print(ans_cnt)
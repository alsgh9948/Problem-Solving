from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
w,h = -1,-1
ans = 1000000000
def bfs(sx,sy,board,len_list):
    q = deque()
    visited = [[False]*w for _ in range(h)]

    q.appendleft((sx,sy,0))
    visited[sx][sy] = True

    while q:
        x,y,cnt = q.pop()
        if not board[x][y] in ['.', 'x'] and (x != sx or y != sy):
            point = int(board[x][y])
            len_list[point] = cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue
            visited[nx][ny] = True
            q.appendleft((nx,ny,cnt+1))

    return len_list

def search_ans(len_list,now,visited_cnt,cnt,visited):
    if visited_cnt == len(len_list):
        global ans
        ans = min(ans,cnt)
        return
    for nxt in range(len(len_list[now])):
        if len_list[now][nxt] == 0 or visited[nxt]:
            continue
        visited[nxt] = True
        search_ans(len_list,nxt,visited_cnt+1,cnt+len_list[now][nxt],visited)
        visited[nxt] = False

def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == 'x':
        return False
    elif visited[x][y]:
        return False
    return True

while True:
    w,h = map(int, stdin.readline().strip().split())
    if w==0 and h==0:
        break
    sx,sy = -1,-1
    start = []
    board = []
    point_num = 0
    for i in range(h):
        board.append(list(stdin.readline().strip()))
        for j in range(w):
            if board[i][j] == 'o':
                sx,sy = i,j
                start.append((i,j))
                board[i][j] = str(point_num)
                point_num += 1
            elif board[i][j] == '*':
                start.append((i,j))
                board[i][j] = str(point_num)
                point_num += 1

    len_list = [[] for _ in range(len(start))]
    ans = 1000000000

    start_point = int(board[sx][sy])
    for x,y in start:
        point = int(board[x][y])
        len_list[point] = bfs(x,y,board,[0]*len(start))

    visited = [False]*len(len_list)
    visited[start_point] = True
    search_ans(len_list, start_point, 1, 0, visited)
    print(ans if ans != 1000000000 else -1)


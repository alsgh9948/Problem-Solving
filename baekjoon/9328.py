from sys import stdin
from collections import deque

h,w,board,door,key,visited = None,None,None,None,None,None
t = int(stdin.readline())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_side(x,y):
    return x == 0 or y == 0 or x == h-1 or y == w-1

def bfs(sx,sy):
    global board,visited
    q = deque()

    q.appendleft((sx,sy))
    visited[sx][sy] = True
    doc_cnt = 0
    while q:
        x,y = q.pop()

        if board[x][y] == '$':
            board[x][y] = '.'
            doc_cnt += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny,visited):
                continue

            visited[nx][ny] = True

            c = board[nx][ny]
            if is_upper(c):
                idx = ord(c) - ord('A')
                if key[idx]:
                    q.appendleft((nx,ny))
                else:
                    door[idx].add((nx,ny))
            elif is_lower(c):
                idx = ord(c) - ord('a')
                if not key[idx]:
                    key[idx] = True
                    for door_x,door_y in door[idx]:
                        if visited[door_x][door_y] or is_side(door_x,door_y):
                            q.appendleft((door_x,door_y))
                q.appendleft((nx,ny))
            else:
                q.appendleft((nx,ny))
    return doc_cnt
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == '*':
        return False
    elif visited[x][y]:
        return False
    return True

def is_upper(c):
    return 'A' <= c <= 'Z'
def is_lower(c):
    return 'a' <= c <= 'z'

for _ in range(t):
    h,w = map(int,stdin.readline().strip().split())

    board = []
    start = []
    door = [set([]) for _ in range(26)]
    key = [False]*26
    visited = [[False]*w for _ in range(h)]

    for i in range(h):
        board.append(list(stdin.readline().strip()))
        for j in range(w):
            c = board[i][j]
            if is_side(i,j):
                if c in ['.', '$']:
                    start.append((i,j))
                elif is_lower(c):
                    key[ord(c) - ord('a')] = True
                    start.append((i,j))
            if is_upper(c):
                door[ord(c) - ord('A')].add((i, j))

    key_str = stdin.readline().strip()
    if key_str != '0':
        for k in key_str:
            key[ord(k)-ord('a')] = True
    for i in range(26):
        if key[i]:
            for x,y in door[i]:
                if is_side(x,y):
                    start.append((x,y))
    ans = 0
    for sx,sy in start:
        ans += bfs(sx,sy)
    print(ans)
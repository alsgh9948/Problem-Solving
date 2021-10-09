from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(input())
def solv(t):
    global board, answer_set
    board = [list(input().strip().split()) for _ in range(4)]

    answer_set = set()
    for sx in range(4):
        for sy in range(4):
            bfs(sx,sy)
    print('#%d %d'%(t,len(answer_set)))

def bfs(sx,sy):
    global answer_set
    q = deque([(sx,sy,board[sx][sy])])
    while q:
        x,y,now = q.pop()

        if len(now) == 7:
            answer_set.add(now)
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny):
                q.appendleft((nx,ny,now+board[nx][ny]))
def point_validator(x,y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True
for t in range(1,tc+1):
    solv(t)
from collections import deque
tc = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = {
    '0':[False,False,False,False],
    '1':[True,True,True,True],
    '2':[True,False,True,False],
    '3':[False,True,False,True],
    '4':[True,True,False,False],
    '5':[False,True,True,False],
    '6':[False,False,True,True],
    '7':[True,False,False,True]
}
def solv(t):
    global board,n,m,l
    n,m,r,c,l = map(int, input().split())

    board = [input().strip().split() for _ in range(n)]
    print('#%d %d'%(t, bfs(r,c)))

def bfs(sx,sy):
    global board
    q = deque([(sx,sy,l-1,board[sx][sy])])
    board[sx][sy] = '0'
    cnt = 0
    while q:
        x,y,remain,now_typ = q.pop()
        cnt += 1
        if remain == 0:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx,ny,dir[now_typ],d):
                q.appendleft((nx,ny,remain-1,board[nx][ny]))
                board[nx][ny] = '0'
    return cnt
def point_validator(x,y,now_typ,d):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] == '0':
        return False
    elif not now_typ[d]:
        return False
    elif not dir[board[x][y]][(d+2)%4]:
        return False
    return True
for t in range(1,tc+1):
    solv(t)
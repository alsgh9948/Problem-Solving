from itertools import permutations

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, input().strip().split())
board = []

candidate = []
for i in range(n):
    board.append(input().strip())
    for j in range(m):
        if board[i][j] == '#':
            candidate.append((i,j))

def solv():
    ans = 0
    for perm in permutations(candidate,2):
        a = perm[0]
        b = perm[1]
        for a_size in range(8):
            if a_size*2+1 > n or a_size*2+1 > m :
                break
            for b_size in range(8):
                if b_size*2+1 > n or b_size*2+1 > m:
                    break
                rst = (1+a_size*4) * (1+b_size*4)
                if ans < rst and insert_cross(a_size, a[0], a[1], b_size, b[0], b[1]):
                    ans = rst
    return ans

def insert_cross(a_size,ax,ay,b_size,bx,by):
    visited = [[False]*m for _ in range(n)]
    visited[ax][ay] = True
    visited[bx][by] = True
    for d in range(4):
        anx, any = ax, ay
        bnx, bny = bx, by
        temp_a_size = a_size
        temp_b_size = b_size
        while temp_a_size != 0 or temp_b_size != 0:
            if temp_a_size != 0:
                anx, any = move_point(anx,any,d,visited)
                if anx == -1:
                    return False
                temp_a_size -= 1
            if temp_b_size != 0:
                bnx, bny = move_point(bnx,bny,d,visited)
                if bnx == -1:
                    return False
                temp_b_size -= 1

    return True

def move_point(x,y,d,visited):
    nx = x + dx[d]
    ny = y + dy[d]

    if not point_validator(nx, ny, visited):
        return -1, -1
    visited[nx][ny] = True
    return nx, ny
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    elif board[x][y] != '#':
        return False
    elif visited[x][y]:
        return False
    return True

print(solv())
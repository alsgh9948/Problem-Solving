from sys import stdin

input = stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

r,c = map(int, input().split())
mx,my,zx,zy = -1,-1,-1,-1

board = []
for x in range(r):
    board.append(list(input().strip()))
    for y in range(c):
        if board[x][y] == 'M':
            mx,my = x,y
        elif board[x][y] == 'Z':
            zx,zy = x,y

def solv():
    m_targets = search_empty_cell(mx,my,False)
    z_targets = search_empty_cell(zx,zy,False)

    for target in m_targets:
        if target in z_targets:
            print(*search_pipe(target))
            return

def search_pipe(target):
    global board
    x,y = target
    for typ in '|-+1234':
        board[x][y] = typ
        if search_empty_cell(mx,my,True):
            return x+1,y+1,typ
def search_empty_cell(sx,sy,flag):
    targets = []
    tx=ty=td = -1
    for d in range(4):
        x = sx + dx[d]
        y = sy + dy[d]

        if boundary_validator(x,y):
            if board[x][y] == '.':
                targets.append((x,y))
            elif is_possible(board[x][y],d):
                tx,ty,td = x,y,d
                break

    if td == -1:
        return targets.sort()

    x,y,d = tx,ty,td
    while True:
        nd = calc_next_dir(d, board[x][y])
        nx = x + dx[nd]
        ny = y + dy[nd]
        if not flag and board[nx][ny] == '.':
            return [(nx,ny)]
        elif flag:
            if boundary_validator(nx,ny):
                if board[nx][ny] == 'Z':
                    return True
                elif not is_possible(board[nx][ny],nd):
                    return False
            else:
                return False

        x,y,d= nx,ny,nd
def boundary_validator(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

def is_possible(typ,d):
    if typ == '|' and d in (0,2):
        return True
    elif typ == '-' and d in (1,3):
        return True
    elif typ == '+':
        return True
    elif typ == '1' and d in (0,3):
        return True
    elif typ == '2' and d in (2,3):
        return True
    elif typ == '3' and d in (1,2):
        return True
    elif typ == '4' and d in (0,1):
        return True
    return False

def calc_next_dir(dir, typ):
    if typ in '|-+':
        return dir
    elif typ == '1':
        if dir == 3:
            return 2
        elif dir == 0:
            return 1
    elif typ == '2':
        if dir == 2:
            return 1
        elif dir == 3:
            return 0
    elif typ == '3':
        if dir == 1:
            return 0
        elif dir == 2:
            return 3
    elif typ == '4':
        if dir == 0:
            return 3
        elif dir == 1:
            return 2

solv()
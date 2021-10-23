dx = [1,0,1, 1]
dy = [0,1,1,-1]

board = [list(map(int, input().split())) for _ in range(19)]
disabled = [[[False]*4 for _ in range(19)] for _ in range(19)]
def solv():
    for sx in range(19):
        for sy in range(19):
            if board[sx][sy] != 0:
                if end_check(sx,sy,board[sx][sy]):
                    return
    print(0)
def end_check(sx,sy,typ):
    global disabled
    for d in range(4):
        if disabled[sx][sy][d]:
            continue
        x,y = sx,sy
        path = []

        while point_validate(x,y,typ):
            path.append((x,y))
            x += dx[d]
            y += dy[d]

        if len(path) == 5:
            path.sort(key=lambda x:(x[1],x[0]))
            print(typ)
            print(path[0][0]+1,path[0][1]+1)
            return True
        else:
            for x,y in path:
                disabled[x][y][d] = True
    return False
def point_validate(x,y,typ):
    if x < 0 or y < 0 or x >= 19 or y >= 19:
        return False
    elif board[x][y] != typ:
        return False
    return True

solv()
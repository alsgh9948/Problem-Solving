from sys import stdin

input = stdin.readline
dir = {
    'U':[-1,0],
    'D':[1,0],
    'L':[0,-1],
    'R':[0,1]
}

def solv():
    tc = 1
    while True:
        r,c = map(int, input().split())
        if r == 0 and c == 0:
            break

        sx=sy=-1
        dest = []
        board = []
        total_box_cnt = 0
        now_box_cnt = 0
        for x in range(r):
            board.append(list(input().strip()))
            for y in range(c):
                if board[x][y] == 'w':
                    sx,sy = x,y
                    board[x][y] = '.'
                elif board[x][y] == 'W':
                    sx,sy = x,y
                    dest.append((x,y))
                    board[x][y] = '+'
                elif board[x][y] == 'b':
                    total_box_cnt += 1
                elif board[x][y] == 'B':
                    total_box_cnt += 1
                    now_box_cnt += 1
                    dest.append((x,y))
                elif board[x][y] == '+':
                    dest.append((x,y))

        order = list(input().strip())
        now_box_cnt = simul(sx,sy,board,order,dest,total_box_cnt,now_box_cnt)
        if now_box_cnt == total_box_cnt:
            answer = 'complete'
        else:
            answer = 'incomplete'
        print('Game %d: %s' % (tc, answer))
        print_answer(board,dest,r,c)
        tc += 1

def print_answer(board,dest,r,c):
    for x in range(r):
        for y in range(c):
            if (x,y) in dest and board[x][y].isalpha():
                print(board[x][y].upper(), end='')
            else:
                print(board[x][y], end='')
        print()

def simul(x,y,board,order,dest,total_box_cnt,now_box_cnt):
    for op in order:
        if now_box_cnt == total_box_cnt:
            break
        nx = x + dir[op][0]
        ny = y + dir[op][1]

        if board[nx][ny] in '.+':
            x,y = nx,ny
        elif board[nx][ny] in 'bB':
            nnx = nx + dir[op][0]
            nny = ny + dir[op][1]
            if board[nnx][nny] in '.+':
                if board[nnx][nny] == '+':
                    now_box_cnt += 1
                board[nx][ny],board[nnx][nny] = '.','b'
                if (nx,ny) in dest:
                    board[nx][ny] = '+'
                    now_box_cnt -= 1
                x,y=nx,ny
    board[x][y] = 'w'
    return now_box_cnt
solv()
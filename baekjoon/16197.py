from itertools import permutations

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().strip().split())

board = []
ans = 11
x1,y1,x2,y2 = -1,-1,-1,-1
for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == 'o':
            if x1 == -1:
                x1,y1 = i,j
            else:
                x2,y2 = i,j

def select_dir(cnt,cx1,cy1,cx2,cy2):
    global ans
    if cnt == 10 or ans <= cnt:
        return
    for d in range(4):
        nx1 = cx1 + dx[d]
        ny1 = cy1 + dy[d]
        point_out_board1 = point_out_board(nx1, ny1)

        nx2 = cx2 + dx[d]
        ny2 = cy2 + dy[d]
        point_out_board2 = point_out_board(nx2, ny2)

        if point_out_board1 and point_out_board2:
            continue
        elif point_out_board1 or point_out_board2:
            ans = min(ans, cnt+1)
            return
        tx1,ty1,tx2,ty2 = cx1,cy1,cx2,cy2
        if board[nx1][ny1] != '#':
            tx1, ty1 = nx1, ny1
        if board[nx2][ny2] != '#':
            tx2, ty2 = nx2, ny2

        if tx1 == tx2 and ty1 == ty2:
            continue

        select_dir(cnt+1,tx1,ty1,tx2,ty2)

def point_out_board(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    return False

select_dir(0,x1,y1,x2,y2)
print(-1 if ans == 11 else ans)

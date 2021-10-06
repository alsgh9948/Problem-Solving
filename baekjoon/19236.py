dx = [-1,-1, 0, 1, 1, 1, 0,-1]
dy = [ 0,-1,-1,-1, 0, 1, 1, 1]
origin_board = []
origin_fish = [[-1,-1,-1]]+[[] for _ in range(16)]
ans = 0
for i in range(4):
    row = []
    input_data = list(map(int, input().split()))
    for j in range(4):
        num = input_data[j*2]
        d = input_data[j*2+1]-1
        row.append(num)
        origin_fish[num] = [i,j,d]
    origin_board.append(row)

def simul(total, shark, tmp_fish, tmp_board):
    global ans
    ans = max(total, ans)
    board = copy_board(tmp_board,[])
    fish = copy_fish(tmp_fish,[])

    move_fish(board,fish)

    x,y,d = shark
    for step in range(1,4):
        nx = x + dx[d]*step
        ny = y + dy[d]*step

        if (nx < 0 or ny < 0 or nx >= 4 or ny >= 4) or board[nx][ny] == 0:
            continue
        else:
            num = board[nx][ny]
            tx,ty,td = fish[num]

            board[x][y] = 0
            fish[num] = [-1,-1,-1]
            board[nx][ny] = -1

            simul(total+num, [nx,ny,td],fish,board)

            fish[num] = [tx,ty,td]
            board[nx][ny] = num
            board[x][y] = -1
def move_fish(board,fish):
    for num in range(1,17):
        x,y,d = fish[num]
        if d >= 0:
            for _ in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if (nx < 0 or ny < 0 or nx >= 4 or ny >= 4) or board[nx][ny] == -1:
                    d = (d+1)%8
                    continue
                else:
                    target = board[nx][ny]
                    fish[num] = [nx,ny,d]
                    fish[target] = [x,y,fish[target][2]]

                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    break
def copy_board(src,dest):
    for i in range(4):
        row = []
        for j in range(4):
            row.append(src[i][j])
        dest.append(row)
    return dest

def copy_fish(src,dest):
    for x,y,d in src:
        dest.append([x,y,d])
    return dest

num = origin_board[0][0]
d = origin_fish[num][2]

origin_fish[num] = [-1,-1,-1]
origin_board[0][0] = -1
simul(num,[0,0,d],origin_fish,origin_board)
print(ans)
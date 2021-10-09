tc = int(input())

def solv(t):
    k = int(input())

    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))

    op_list = []
    for _ in range(k):
        num,dir = map(int, input().split())
        op_list.append((num-1,dir))

    simul(board,op_list)
    print('#%d %d'%(t,calc_score(board)))

def simul(board,op_list):
    for num, dir in op_list:
        visited = [False]*4
        visited[num] = True
        rotate(num,dir,board,visited)
def rotate(num,dir,board,visited):
    if num < 3 and board[num][2] != board[num+1][6]:
        if not visited[num+1]:
            visited[num+1] = True
            rotate(num+1,-dir,board,visited)
    if num > 0 and board[num][6] != board[num-1][2]:
        if not visited[num-1]:
            visited[num-1] = True
            rotate(num-1,-dir,board,visited)
    if dir == 1:
        board[num] = board[num][-1:]+board[num][:-1]
    else:
        board[num] = board[num][1:]+board[num][:1]

def calc_score(board):
    score = 0
    for idx in range(4):
        row = board[idx]
        if row[0] == 1:
            score += 2**idx
    return score
for t in range(1,tc+1):
    solv(t)

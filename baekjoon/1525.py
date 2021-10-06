from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
sp = -1
start_board = ''

for i in range(3):
    row = input().strip().split()
    for j in range(3):
        if row[j] == '0':
            sp = i*3+j
        start_board += row[j]

def bfs():
    visited = set([start_board])
    q = deque()
    q.appendleft((sp,0,start_board))
    while q:
        now,cnt,board = q.pop()
        if now == 8 and board == '123456780':
            print(cnt)
            return

        x = now//3
        y = now%3
        board_list = list(board)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not point_valitator(nx,ny):
                continue
            nxt = nx*3+ny
            board_list[now], board_list[nxt] = board_list[nxt], board_list[now]
            str_board = ''.join(board_list)
            if not str_board in visited:
                visited.add(str_board)
                q.appendleft((nxt,cnt+1,str_board))
            board_list[now], board_list[nxt] = board_list[nxt], board_list[now]
    print(-1)
def point_valitator(x,y):
    if x < 0 or y < 0 or x >= 3 or y >= 3:
        return False
    return True

bfs()
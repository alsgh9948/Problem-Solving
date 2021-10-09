from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input().strip())

board = []
fish_cnt = [0,0,0,0,0,0,0]
sx=sy=-1
for i in range(n):
    board.append(list(map(int,input().strip().split())))
    for j in range(n):
        if board[i][j] == 9 and sx == -1:
            sx,sy = i,j
            board[i][j] = 0
        elif board[i][j] != 0:
            fish_cnt[board[i][j]] += 1
def solv():
    global board, fish_cnt
    visited = [[False]*n for _ in range(n)]
    q = deque()

    q.appendleft((sx,sy,0))
    visited[sx][sy] = True

    tcnt=tx=ty=987654321
    shark_size = 2
    eat_cnt = 0

    total_time = 0
    time = 0
    while q:
        q_len = len(q)
        for _ in range(q_len):
            x,y,cnt = q.pop()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not point_validator(nx,ny,visited,shark_size):
                    continue

                visited[nx][ny] = True
                if board[nx][ny] > 0 and board[nx][ny] < shark_size:
                    tcnt, tx, ty = min((tcnt, tx, ty), (cnt+1, nx, ny))
                    continue
                q.appendleft((nx,ny,cnt+1))

        time += 1
        if tcnt != 987654321:
            fish_cnt[board[tx][ty]] -= 1
            board[tx][ty] = 0
            eat_cnt += 1
            if eat_cnt == shark_size:
                shark_size += 1
                eat_cnt = 0
            if sum(fish_cnt[:shark_size]) == 0:
                return total_time + time

            q = deque()
            visited = [[False]*n for _ in range(n)]

            q.appendleft((tx,ty,0))
            visited[tx][ty] = True
            tcnt=tx=ty=987654321
            total_time += time
            time = 0

    return total_time

def point_validator(x,y,visited,shark_size):
    if x < 0  or y < 0 or x >= n or y >= n:
        return False
    elif visited[x][y]:
        return False
    elif board[x][y] > shark_size:
        return False
    return True

if sum(fish_cnt[:2]) == 0:
    print(0)
else:
    print(solv())
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input().strip())
k = int(input().strip())

board = [[False]*n for _ in range(n)]
for _ in range(k):
    x,y = map(int, input().strip().split())
    board[x-1][y-1] = True

command_list = []
l = int(input().strip())

for _ in range(l):
    t,c = input().strip().split()
    command_list.append((int(t),c))




def solv():
    global board
    t = 0
    dq = deque()
    snake = [[False]*n for _ in range(n)]
    command_idx = 0

    x,y,d = 0,0,1
    snake[x][y] = True

    dq.appendleft((x,y))
    while True:
        t += 1

        x = x + dx[d]
        y = y + dy[d]

        if not point_validator(x, y, snake):
            break

        dq.appendleft((x, y))
        snake[x][y] = True

        if not board[x][y]:
            tx,ty = dq.pop()
            snake[tx][ty] = False
        else:
            board[x][y] = False

        if command_idx < l and command_list[command_idx][0] == t:
            d = rotate_head(command_list[command_idx][1],d)
            command_idx += 1
    return t
def rotate_head(c,d):
    if c == 'L':
        return (d+3)%4
    else:
        return (d+1)%4

def point_validator(x,y,snake):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif snake[x][y]:
        return False
    return True

print(solv())
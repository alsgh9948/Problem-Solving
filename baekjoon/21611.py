from sys import stdin

input = stdin.readline
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
num_board = [[0]*n for _ in range(n)]
balls = [0]*(n*n)
balls[0] = -1
op_list = []
for _ in range(m):
    d,s = map(int, input().split())
    op_list.append((d,s))

def solv():
    set_num_board()
    score = 0
    for d,s in op_list:
        d = trans_dir(d)
        shoot_ball(d,s)
        remove_ball()
        score += explosion_ball()
        renew_ball()
    print(score)
def set_num_board():
    global num_board,balls
    x=y=n//2
    num=1
    step=1
    cnt=turn_cnt=0
    d = 0
    while num < n*n:
        x += dx[d]
        y += dy[d]
        num_board[x][y] = num
        balls[num] = board[x][y]

        num += 1
        cnt += 1
        if cnt == step:
            cnt = 0
            d = (d+1)%4
            turn_cnt += 1

            if turn_cnt == 2:
                step += 1
                turn_cnt = 0

def shoot_ball(d,s):
    x=y=n//2

    for _ in range(s):
        x += dx[d]
        y += dy[d]

        ball_num = num_board[x][y]
        balls[ball_num] = 0

def remove_ball():
    step = 0
    for idx in range(1,n*n):
        if balls[idx] == 0:
            step += 1
        elif step > 0:
            balls[idx-step],balls[idx] = balls[idx],0

def explosion_ball():
    global balls
    score = 0
    while True:
        start = 1
        cnt = 1
        target = balls[start]
        remove_points = []
        for idx in range(2,n*n):
            if balls[idx] == 0:
                break

            if balls[idx] == target:
                cnt += 1
            else:
                if cnt >= 4:
                    remove_points.append((start,cnt))
                start = idx
                target = balls[start]
                cnt = 1
        if cnt >= 4:
            remove_points.append((start, cnt))
        if remove_points:
            new_balls = [0]*(n*n)
            new_balls[0] = -1

            start = 1
            new_balls_idx = 1
            for end, cnt in remove_points:
                score += balls[end]*cnt
                for idx in range(start, end):
                    new_balls[new_balls_idx] = balls[idx]
                    new_balls_idx += 1
                start = end+cnt
            for idx in range(start, n*n):
                new_balls[new_balls_idx] = balls[idx]
                new_balls_idx += 1
            balls = new_balls
        else:
            break
    return score

def renew_ball():
    global balls
    new_ball = [0]*(n*n)
    new_ball[0] = -1

    target = balls[1]
    cnt = 1
    new_ball_idx = 1
    for num in balls[2:]:
        if num == target:
            cnt += 1
        else:
            new_ball[new_ball_idx] = cnt
            new_ball[new_ball_idx+1] = target
            target = num
            cnt = 1
            new_ball_idx += 2
            if new_ball_idx >= n*n:
                break
    balls = new_ball
def trans_dir(d):
    if d == 1:
        return 3
    elif d == 2:
        return 1
    elif d == 3:
        return 0
    else:
        return 2

solv()
from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

n,m,k = map(int, input().split())

board = [[[[],[]] for _ in range(n)] for _ in range(n)]
fire_balls = deque()
for _ in range(m):
    r,c,m,s,d = map(int, input().split())
    fire_balls.appendleft((r-1,c-1,m,s,d))
    board[r-1][c-1][0].append((m,s,d))

def solv():
    timing = 0
    for _ in range(k):
        next_timing = (timing+1)%2
        move_ball(timing,next_timing)
        renew_ball(next_timing)
        timing = next_timing

    answer = 0
    for x,y,m,s,d in fire_balls:
        answer += m
    print(answer)
def renew_ball(next_timing):
    global board, fire_balls
    ball_cnt = len(fire_balls)

    for _ in range(ball_cnt):
        x,y,m,s,d = fire_balls.pop()

        if len(board[x][y][next_timing]) == 1:
            fire_balls.appendleft((x,y,m,s,d))
        else:
            total_m = 0
            total_s = 0
            target = board[x][y][next_timing][0][2]%2
            cnt = 0
            typ = 0
            for m,s,d in board[x][y][next_timing]:
                total_m += m
                total_s += s
                if d%2 != target:
                    typ = 1
                cnt += 1

            new_m = total_m//5
            board[x][y][next_timing] = []
            if new_m == 0:
                continue
            new_s = total_s//cnt
            for new_d in range(typ,8,2):
                fire_balls.appendleft((x,y,new_m,new_s,new_d))
                board[x][y].append((new_m,new_s,new_d))


def move_ball(timing,next_timing):
    global fire_balls,board
    ball_cnt = len(fire_balls)

    for _ in range(ball_cnt):
        x,y,m,s,d = fire_balls.pop()
        board[x][y][timing] = []

        nx = (x + dx[d]*s)%n
        ny = (y + dy[d]*s)%n

        if not board[nx][ny][next_timing]:
            fire_balls.appendleft((nx,ny,m,s,d))
        board[nx][ny][next_timing].append((m,s,d))

solv()
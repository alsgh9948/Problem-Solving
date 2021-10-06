from sys import stdin

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
student = []

for _ in range(n**2):
    student.append(list(map(int, input().split())))

board = [[[0,0] for _ in range(n)] for _ in range(n)]

def solv():
    global board
    for idx in range(n**2):
        num = student[idx][0]
        like_list = student[idx][1:]
        pos = [0,0,-1000,-1000]
        for x in range(n):
            for y in range(n):
                if board[x][y][0] == 0:
                    cnt,empty_cnt = check_position(x,y,like_list)
                    pos = max(pos,[cnt,empty_cnt,-x,-y])

        x,y = -pos[2],-pos[3]
        board[x][y] = [num,idx]

    print(calc_ans())

def calc_ans():
    ans = 0
    for x in range(n):
        for y in range(n):
            like_list = student[board[x][y][1]][1:]
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if point_validator(nx, ny):
                    num = board[nx][ny][0]
                    if num in like_list:
                        cnt += 1
            if cnt != 0:
                ans += 10**(cnt-1)
    return ans
def check_position(x,y,like_list):
    cnt = 0
    empty_cnt = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if point_validator(nx,ny):
            num = board[nx][ny][0]
            if num == 0:
                empty_cnt += 1
            elif num in like_list:
                cnt += 1
    return cnt,empty_cnt
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()
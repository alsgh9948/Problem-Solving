from sys import stdin

input = stdin.readline

n,m = map(int, input().split())

board = []
ans = 987654321

for _ in range(n):
    row = input().strip()
    tmp = []
    for j in range(m):
        if row[j] == 'B':
            tmp.append(0)
        else:
            tmp.append(1)
    board.append(tmp)
def solv():
    for i in range(n-7):
        for j in range(m-7):
            check(i,j)

def check(sx,sy):
    global ans
    for start in [0,1]:
        cnt = 0
        color = start
        flag = False
        for i in range(sx, sx+8):
            for j in range(sy, sy+8):
               if board[i][j] != color:
                   cnt += 1
                   if cnt >= ans:
                       flag = True
                       break
               color = (color+1)%2
            start = (start+1)%2
            color = start

            if flag:
                break
        if not flag:
            ans = min(ans,cnt)

solv()
print(ans)
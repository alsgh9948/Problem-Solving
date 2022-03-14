n = int(input())
target = []
board = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(n):
        if board[x][y] == 1:
            target.append((x,y))

r = [False]*(n*2-1)
l = [False]*(n*2-1)

answer = 0
def solv(now,count):
    global answer
    if now == len(target):
        answer = max(answer, count)
        return

    x,y = target[now]

    rnum = x+y
    lnum = n-y-1+x
    if not r[rnum] and not l[lnum]:
        r[rnum] = l[lnum] = True
        solv(now+1,count+1)
        r[rnum] = l[lnum] = False

    solv(now+1,count)

solv(0,0)
print(answer)
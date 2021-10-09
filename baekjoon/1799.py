n = int(input())

board = []
targets = [[] for _ in range(20)]
rd = [False]*20
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(n):
        ld_num = x+y
        if board[x][y] == 1:
            targets[ld_num].append((x,y))

answer = [0,0]

def solv():
    insert_bishop(0,0)
    insert_bishop(1,0)

    print(answer[0]+answer[1])
def insert_bishop(idx,cnt):
    global answer,ld,rd

    if idx >= 2*n-1:
        answer[idx%2] = max(answer[idx%2], cnt)
        return

    for x,y in targets[idx]:
        if board[x][y] == 1:
            rd_num = (n-1-x)+y
            if not rd[rd_num]:
                rd[rd_num] = True
                insert_bishop(idx+2,cnt+1)
                rd[rd_num] = False
    insert_bishop(idx+2,cnt)
solv()
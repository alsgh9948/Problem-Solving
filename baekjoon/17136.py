board = []
candidate = []
for i in range(10):
    board.append(list(input().strip().split()))
    for j in range(10):
        if board[i][j] == '1':
            candidate.append((i,j))
paper = [0,5,5,5,5,5]

visited = [[False]*10 for _ in range(10)]
ans = 987654321
def select_paper(idx, cnt):
    global ans,paper
    if cnt >= ans:
        return
    if idx == len(candidate):
        ans = min(ans,cnt)
        return

    x = candidate[idx][0]
    y = candidate[idx][1]


    if visited[x][y] != 0:
        select_paper(idx+1,cnt)
        return
    for size in range(5,0,-1):

        if paper[size] == 0 or x + size > 10 or y + size > 10:
            continue
        if insert_paper(x,y,size,True):
            paper[size] -= 1
            select_paper(idx+1,cnt+1)
            insert_paper(x, y, size, False)
            paper[size] += 1
def insert_paper(x,y,size,value):
    global visited
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[i][j] == '0' or (value and visited[i][j]):
                for ii in range(i,x-1,-1):
                    for jj in range(j-1,y-1,-1):
                        visited[ii][jj] = False
                    j = y+size
                return False
            visited[i][j] = value
    return True

select_paper(0,0)
print(-1 if ans == 987654321 else ans)
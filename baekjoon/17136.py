board = []
targets = []
remain_paper = [0,5,5,5,5,5]
answer = 9876543210
visited = [[False]*10 for _ in range(10)]
for x in range(10):
    board.append(list(map(int, input().split())))
    for y in range(10):
        if board[x][y] == 1:
            targets.append((x,y))

def solv():
    select_paper(0,0)
    print(-1 if answer == 9876543210 else answer)

def select_paper(idx,count):
    global remain_paper, answer
    if count >= answer:
        return

    if idx == len(targets):
        answer = min(answer, count)
        return

    x,y = targets[idx]
    if visited[x][y]:
        select_paper(idx+1,count)
    else:
        for size in range(5,0,-1):
            if remain_paper[size] > 0 and is_possible(x,y,size):
                remain_paper[size] -= 1
                toggle_visited_status(x,y,size)

                select_paper(idx+1, count+1)

                remain_paper[size] += 1
                toggle_visited_status(x,y,size)

def toggle_visited_status(sx,sy,size):
    global visited
    mx,my = sx+size,sy+size
    for x in range(sx,mx):
        for y in range(sy,my):
            visited[x][y] = not visited[x][y]
def is_possible(sx,sy,size):
    mx,my = sx+size,sy+size
    if mx > 10 or my > 10:
        return False

    for x in range(sx,mx):
        for y in range(sy,my):
            if board[x][y] == 0 or visited[x][y]:
                return False
    return True

solv()
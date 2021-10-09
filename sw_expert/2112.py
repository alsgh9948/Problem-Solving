tc = int(input())

def solv(t):
    global d,w,k,board,a_layer,b_layer,answer
    d,w,k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]
    a_layer = [0]*w
    b_layer = [1]*w
    answer = 9876543210
    if k == 1 or check_performance():
        answer = 0
    else:
        select_layer(0,0)
    print('#%d %d'%(t,answer))

def select_layer(idx,cnt):
    global board,answer
    if answer < cnt:
        return

    if cnt > 0 and check_performance():
        answer = min(answer, cnt)
        return

    if idx == d:
        return

    tmp = board[idx]
    board[idx] = a_layer
    select_layer(idx+1,cnt+1)

    board[idx] = b_layer
    select_layer(idx+1,cnt+1)

    board[idx] = tmp
    select_layer(idx+1,cnt)

def check_performance():
    for y in range(w):
        before = board[0][y]
        cnt = 1
        flag = False
        for x in range(1,d):
            if board[x][y] == before:
                cnt += 1
                if cnt == k:
                    flag = True
                    break
            else:
                before = board[x][y]
                cnt = 1
        if not flag:
            return False
    return True
for t in range(1,tc+1):
    solv(t)
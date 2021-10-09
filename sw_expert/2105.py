tc = int(input())

dx = [1,1,-1,-1]
dy = [-1,1,1,-1]
def solv(t):
    global n, board,visited,visited_num
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*101
    visited_num = 0

    print('#%d %d'%(t,simul()))
def simul():
    global visited_num
    answer = -1
    for x in range(n-1):
        for y in range(1,n-1):
            for cnt1 in range(1,n-1):
                if y - cnt1 < 0:
                    break
                for cnt2 in range(1,n-1):
                    visited_num += 1
                    if y + cnt2 >= n:
                        break
                    if cnt1*2+cnt2*2 <= answer:
                        continue
                    if check(x,y,cnt1,cnt2):
                        answer = max(answer,cnt1*2+cnt2*2)
    return answer
def check(x,y,cnt1,cnt2):
    global visited
    for d in range(4):
        cnt = cnt1
        if d in [1, 3]:
            cnt = cnt2
        for _ in range(cnt):
            x += dx[d]
            y += dy[d]
            if point_validator(x,y):
                visited[board[x][y]] = visited_num
            else:
                return False
    return True
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif visited[board[x][y]] == visited_num:
        return False
    return True
for t in range(1,tc+1):
    solv(t)
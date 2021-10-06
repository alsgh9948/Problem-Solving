from collections import deque

ans = 987654321
n = int(input())
popular = [0]+list(map(int,input().split()))

board = [[]]
for idx in range(1,n+1):
    input_data = list(map(int,input().split()))
    board.append(input_data[1:])

select_num = [False]*(n+1)
select_num[1] = True
def solv():
    select_area(2,1)

def select_area(now,cnt):
    global select_num
    simul()

    if cnt >= n-1:
        return

    for idx in range(now,n+1):
        select_num[idx] = True
        select_area(idx+1,cnt+1)
        select_num[idx] = False

def simul():
    global ans
    select = []
    non_select = []
    for idx in range(1,n+1):
        if select_num[idx]:
            select.append(idx)
        else:
            non_select.append(idx)

    visited = [False]*(n+1)

    sum1 = bfs(visited,select)
    sum2 = bfs(visited,non_select)

    if sum1 != -1 and sum2 != -1:
        ans = min(ans,abs(sum1-sum2))
def bfs(visited,typ_list):
    q = deque()
    start = typ_list[0]
    visited[start] = True
    q.appendleft(start)
    cnt = 0
    p_sum = 0
    while q:
        now = q.pop()
        p_sum += popular[now]
        cnt += 1
        for nxt in board[now]:
            if nxt in typ_list and not visited[nxt]:
                q.appendleft(nxt)
                visited[nxt] = True

    return p_sum if cnt == len(typ_list) else -1

solv()
print(-1 if ans == 987654321 else ans)
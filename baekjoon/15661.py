from sys import stdin

input = stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

select = [False]*n
select[0] = True
ans = 987564321
def select_member(now,cnt):
    global select, ans

    if cnt == n-2 or now == n:
        ans = min(ans, calc_status())
        return

    select_member(now+1,cnt)

    select[now] = True
    select_member(now+1,cnt+1)
    select[now] = False

def calc_status():
    start,link = [],[]
    for idx in range(n):
        if select[idx]:
            start.append(idx)
        else:
            link.append(idx)

    start_status = 0
    for i in range(len(start)-1):
        a = start[i]
        for j in range(i+1,len(start)):
            b = start[j]
            start_status += board[a][b]+board[b][a]

    link_status = 0
    for i in range(len(link) - 1):
        a = link[i]
        for j in range(i + 1, len(link)):
            b = link[j]
            link_status += board[a][b] + board[b][a]

    return abs(start_status-link_status)

select_member(1,1)
print(ans)
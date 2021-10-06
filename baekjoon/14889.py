n = int(input())

_map = [list(map(int,input().strip().split())) for _ in range(n)]

select = [False]*n

select[0] = True
ans = 1000000000
def select_member(cnt, idx, select):
    if cnt == n/2:
        simul(select)
        return
    for i in range(idx,n):
        select[i] = True
        select_member(cnt+1,i+1,select)
        select[i] = False

def simul(select):
    start = []
    link = []
    for i in range(n):
        if select[i]:
            start.append(i)
        else:
            link.append(i)

    start_power = calc_power(start)
    link_power = calc_power(link)
    global ans
    ans = min(ans, abs(start_power-link_power))

def calc_power(member):
    sum_power = 0
    for i in range(len(member)-1):
        for j in range(i+1,len(member)):
            x = member[i]
            y = member[j]
            sum_power += (_map[x][y] + _map[y][x])
    return sum_power

select_member(1,1,select)
print(ans)
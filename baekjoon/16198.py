n = int(input())
w_list = list(map(int,input().strip().split()))

ans = 0
def simul(cnt, w_sum, select):
    if cnt == n-2:
       global ans
       ans = max(ans, w_sum)
       return
    for i in range(1,n):
        if select[i]:
            continue

        select[i] = True
        left_w = get_w(-1, i, select)
        right_w = get_w(1, i, select)
        if left_w != 0 and right_w != 0:
            simul(cnt+1,w_sum + (left_w * right_w), select)
        select[i] = False

def get_w(dir, x, select):
    nx = x + dir
    while 0 <= nx and nx <= n-1:
        if not select[nx]:
            return w_list[nx]
        nx += dir
    return 0

simul(0,0,[False]*n)

print(ans)
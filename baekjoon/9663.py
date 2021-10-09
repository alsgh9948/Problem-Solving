n = int(input())
cur = [False]*15
rd = [False]*30
ld = [False]*30

ans = 0
def solv(x):
    global ans
    if x == n:
        ans += 1
        return

    for y in range(n):
        l_num,r_num = is_possible(x,y)
        if l_num != -1:
            ld[l_num] = True
            rd[r_num] = True
            cur[y] = True

            solv(x+1)

            ld[l_num] = False
            rd[r_num] = False
            cur[y] = False
def is_possible(x,y):
    if cur[y]:
        return -1,-1
    elif ld[x+y]:
        return -1,-1
    elif rd[(n-1-x)+y]:
        return -1,-1

    return x+y,(n-1-x)+y
solv(0)
print(ans)
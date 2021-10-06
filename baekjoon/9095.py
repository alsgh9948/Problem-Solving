tc = int(input())
ans = 0
def solv(sum,n):
    if sum > n:
        return
    if sum == n:
        global ans
        ans+=1
    for i in range(1,4):
        solv(sum+i,n)

for _ in range(tc):
    ans = 0
    solv(0,int(input()))
    print(ans)

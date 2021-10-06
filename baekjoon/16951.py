n,k = map(int,input().strip().split())

num_list = list(map(int,input().strip().split()))

ans = 987654321
for i in range(n):
    before = num_list[i]-k*i
    if before <= 0:
        before = k
    cnt = 0 if before == num_list[0] else 1
    for j in range(1,n):
        if num_list[j] != before+k:
            cnt += 1
        before += k
    ans = min(ans,cnt)
print(ans)
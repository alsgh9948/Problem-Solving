import sys
def perv_permutaion(target_list, n):
    i = n-1
    while i > 0 and target_list[i-1] <= target_list[i]:
        i -= 1
    if i <= 0:
        return -1
    j = n-1
    while target_list[i-1] <= target_list[j]:
        j -= 1
    target_list[i-1], target_list[j] = target_list[j], target_list[i-1]

    j = n-1
    while(i < j):
        target_list[i], target_list[j] = target_list[j], target_list[i]
        i += 1
        j -= 1
    return target_list

n = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))

ans = perv_permutaion(target_list, n)
if ans == -1:
    print(ans)
else:
    for num in ans:
        print(num, end=' ')


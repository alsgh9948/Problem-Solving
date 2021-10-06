n = int(input())

arr = list(map(int, input().split()))
#
# def next_permutation(target_list, n):
#     i = n-1
#     while i>0 and target_list[i-1] >= target_list[i]:
#         i-=1
#     if i <= 0:
#         return False
#     j = n-1
#     while target_list[i-1] >= target_list[j]:
#         j-=1
#     target_list[i-1], target_list[j] = target_list[j], target_list[i-1]
#     j=n-1
#     while i < j:
#         target_list[i], target_list[j] = target_list[j], target_list[i]
#         i+=1
#         j-=1
#     return target_list
#
def calc_sum(arr):
    sum = 0
    for i in range(0, len(arr) - 1):
        sum += abs(arr[i] - arr[i + 1])
    return sum
#
# arr.sort()
# ans = max(-10000000, calc_sum(arr))
# next_arr = next_permutation(arr, n)
# while next_arr:
#     ans = max(ans, calc_sum(next_arr))
#     next_arr = next_permutation(next_arr, n)
#
# print(ans)

from itertools import permutations

permu_list = permutations(arr,n)

ans = -1000000
for target in permu_list:
    ans = max(ans, calc_sum(target))

print(ans)
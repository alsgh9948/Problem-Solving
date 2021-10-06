# import sys
#
# def next_permutation(target_list, n):
#     i = n-1
#     while i > 0 and target_list[i-1] >= target_list[i]:
#         i -= 1
#     if i <= 0:
#         return False
#
#     j = n-1
#     while target_list[i-1] >= target_list[j]:
#         j -= 1
#     target_list[i-1],  target_list[j] = target_list[j], target_list[i-1]
#
#     j = n-1
#     while i < j:
#         target_list[i], target_list[j] = target_list[j], target_list[i]
#         i += 1
#         j -= 1
#
#     return target_list
#
#
# n = int(sys.stdin.readline())
# target_list = []
# for i in range(n):
#     target_list.append(i+1)
#
#
# for num in target_list:
#     print(num, end=' ')
# print()
#
# while next_permutation(target_list,n):
#     for num in target_list:
#         print(num, end=' ')
#     print()
#

from itertools import permutations

n = int(input())
target_list = [i+1 for i in range(n)]
ans = permutations(target_list,n)

for num in ans:
    print(*num)

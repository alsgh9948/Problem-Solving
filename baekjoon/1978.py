# import sys, math
#
# n = int(sys.stdin.readline())
#
# def is_prim(target):
#     if(target == 1):
#         return False
#     for i in range(2,int(math.sqrt(target)+1)):
#         if target%i == 0:
#             return False
#     return True
# input_arr = list(map(int,sys.stdin.readline().split()))
#
# ans = 0
# for num in input_arr:
#     if(is_prim((num))):
#         ans += 1
#
# print(ans)

import sys

n = int(sys.stdin.readline())

prim_check = [True for _ in range(1001)]
prim_check[1] = False
def prim_check_func():
    for i in range(2,1001):
        if(not prim_check[i]):
            continue
        for j in range(2,1001):
            target = i*j
            if(target > 1000):
                break
            prim_check[target] = False

prim_check_func()
input_arr = list(map(int,sys.stdin.readline().split()))
ans = 0
for num in input_arr:
    if(prim_check[num]):
        ans+=1

print(ans)
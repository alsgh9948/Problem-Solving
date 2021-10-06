# import sys, math
# prim_check = [True for _ in range(1000001)]
# prim_check[1] = False
#
# for i in range(2,1001):
#     if prim_check[i]:
#         for j in range(i*i, 1000001, i):
#             prim_check[j] = False
#
# def solv():
#     while True:
#         n = int(sys.stdin.readline())
#         if n == 0:
#             break
#         if not solution(n):
#             print('Goldbach\'s conjecture is wrong.')
#
# def solution(n):
#     for i in range(3, n, 2):
#         j = n-i
#         if prim_check[i] and prim_check[j]:
#             print('%d = %d + %d'%(n,i,j))
#             return True
#     return False
#
# solv()

import sys

check = [False for _ in range(1000000 + 1)]
j = 0
for i in range(2, 1000 + 1):
    if check[i] == False:
        j = i * 2
        while j <= 1000000:
            check[j] = True
            j += i
while True:
    flag=0
    num=int(sys.stdin.readline())
    if num==0:
        break

    for i in range(3,num):
        j=num-i
        if check[j]==False and check[i]==False:
            print("%d = %d + %d"%(num,i,j))
            flag=1
            break
        else:
            continue
    if flag!=1:
        print("Goldbach's conjecture is wrong.")
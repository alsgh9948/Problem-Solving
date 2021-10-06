# from sys import stdin
#
# input = stdin.readline
#
# n = int(input())
#
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]
#
# dragon = [[0]]
# for idx in range(10):
#     nxt_dragon = []
#     for d in dragon[idx]:
#         nxt_dragon.append(d)
#
#     for d in dragon[idx][::-1]:
#         nxt_dragon.append((d+1)%4)
#
#     dragon.append(nxt_dragon)
#
# board = [[False]*101 for _ in range(101)]
#
# def solv():
#     for _ in range(n):
#         y,x,d,g = map(int, input().split())
#         board[x][y] = True
#         for dir in dragon[g]:
#             x += dx[(d+dir)%4]
#             y += dy[(d+dir)%4]
#             board[x][y] = True
#
#     ans = 0
#     for x in range(101):
#         for y in range(101):
#             if board[x][y]:
#                 if x+1 < 101 and y+1 < 101:
#                     if board[x+1][y] and board[x][y+1] and board[x+1][y+1]:
#                         ans += 1
#     print(ans)
#
# solv()

a = {1,2,3,4,5,6}
b = {2,5}
print(b.issubset(a))
from sys import stdin
from itertools import combinations

input = stdin.readline

n = int(input())
mp,mf,ms,mv = map(int, input().split())

board = [[]]
for _ in range(n):
    p,f,s,v,c = map(int, input().split())
    board.append((p,f,s,v,c))

def solv():
    answer_c = 9875643210
    answer = None
    for cnt in range(1,n+1):
        for comb in combinations(range(1,n+1),cnt):
            tp=tf=ts=tv=tc=0
            for target in comb:
                tp += board[target][0]
                tf += board[target][1]
                ts += board[target][2]
                tv += board[target][3]
                tc += board[target][4]

            if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
                if answer_c > tc:
                    answer_c = tc
                    answer = comb
                elif answer_c == tc:
                    answer = sorted((answer,comb))[0]
    if answer_c == 9875643210:
        print(-1)
    else:
        print(answer_c)
        print(*answer)

solv()
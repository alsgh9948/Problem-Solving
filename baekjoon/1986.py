from sys import stdin

input = stdin.readline
dx = [-2,-1, 1, 2, 2, 1,-1,-2]
dy = [ 1, 2, 2, 1,-1,-2,-2,-1]

n,m = map(int, input().split())



def solv():


    k_list = list(map(int, input().split()))
    k = []
    for idx in range(1, len(k_list), 2):
        k.append((k_list[idx], k_list[idx + 1]))
def queen_check():
    q_list = list(map(int, input().split()))
    for idx in range(1, len(q_list), 2):
        x,y = q_list[idx], q_list[idx+1]

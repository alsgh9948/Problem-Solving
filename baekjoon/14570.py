from sys import stdin

input = stdin.readline

n = int(input())
adj_list = [[-1,-1] for _ in range(n)]
def solv():
    set_tree()
    k = int(input())
    print(drop_ball(k)+1)
def drop_ball(k):
    now = 0
    while True:
        if adj_list[now][0] == adj_list[now][1] == -2:
            break
        elif adj_list[now][0] == -2:
            now = adj_list[now][1]
        elif adj_list[now][1] == -2:
            now = adj_list[now][0]
        else:
            if k%2 == 1:
                k = k//2 + 1
                now = adj_list[now][0]
            else:
                k //= 2
                now = adj_list[now][1]
    return now
def set_tree():
    global adj_list
    for idx in range(n):
        u, v = map(lambda x: int(x) - 1, input().split())
        adj_list[idx][0] = u
        adj_list[idx][1] = v
solv()
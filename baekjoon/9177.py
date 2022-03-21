from sys import stdin

input = stdin.readline

n = int(input())

def solv():
    global a_len,b_len,t_len,visited
    a,b,t = input().strip().split()
    a_len = len(a)
    b_len = len(b)
    t_len = len(t)
    visited = [[False]*(b_len+1) for _ in range(a_len+1)]
    return "yes" if is_possible(0,a,0,b,0,t) else "no"

def is_possible(a_idx,a,b_idx,b,now,t):
    global visited
    if now == t_len:
        return True

    if a_idx < a_len and a[a_idx] == t[now] and not visited[a_idx+1][b_idx]:
        visited[a_idx+1][b_idx] = True
        if is_possible(a_idx+1,a,b_idx,b,now+1,t):
            return True

    if b_idx < b_len and b[b_idx] == t[now] and not visited[a_idx][b_idx+1]:
        visited[a_idx][b_idx+1] = True
        if is_possible(a_idx,a,b_idx+1,b,now+1,t):
            return True
    return False
for idx in range(n):
    print(f"Data set {idx+1}: {solv()}")
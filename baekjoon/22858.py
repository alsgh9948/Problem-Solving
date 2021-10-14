from sys import stdin

input = stdin.readline

n,k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

def solv():
    global s
    for _ in range(k):
        s = mix_num(s)
    print(*s)

def mix_num(tmp):
    before = [0]*n
    tmp_idx = 0
    for idx in d:
        before[idx-1] = tmp[tmp_idx]
        tmp_idx += 1
    return before
solv()
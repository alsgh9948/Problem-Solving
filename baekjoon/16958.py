from sys import stdin

def input(split=True):
    if not split:
        return stdin.readline().strip()
    return stdin.readline().strip().split()
n,t = map(int, input())

city = [()]

for _ in range(n):
    city.append(tuple(map(int, input())))

m = int(input(False))

min_special_length = [0]*(n+1)
def set_special_length():
    global min_special_length

    for i in range(1,n+1):
        if city[i][0] == 1:
            continue
        min_special_length[i] = 987654321
        for j in range(1, n+1):
            if city[j][0] == 0:
                continue
            length = calc_length(i,j)
            min_special_length[i] = min(min_special_length[i], length)
        if min_special_length[i] == 987654321:
            min_special_length[i] = 0

def solv():
    for _ in range(m):
        a, b = map(int, input())
        length = calc_length(a,b)
        print(min(length, min_special_length[a]+t+min_special_length[b]))

def calc_length(now,nxt):
    return abs(city[now][1] - city[nxt][1]) + abs(city[now][2] - city[nxt][2])

set_special_length()
solv()
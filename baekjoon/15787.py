from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
orders = []
for _ in range(m):
    order = list(map(int, input().split()))
    if len(order) == 2:
        order.append(-1)
    orders.append(order)
def solv():
    trains = [0]*(n+1)
    for typ, train_num, passenger_num in orders:
        passenger_num -= 1
        if typ == 1:
            trains[train_num] |= (1 << passenger_num)
        elif typ == 2:
            trains[train_num] &= ~(1 << passenger_num)
        elif typ == 3:
            trains[train_num] = trains[train_num] << 1
            if trains[train_num] >= 2**20:
                trains[train_num] %= 2**20
        elif typ == 4:
            trains[train_num] = trains[train_num] >> 1

    answer = 0
    visited = [False]*(2**20)
    for status in trains[1:]:
        if not visited[status]:
            answer += 1
            visited[status] = True

    print(answer)
solv()
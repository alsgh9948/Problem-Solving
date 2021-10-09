from sys import stdin

input = stdin.readline

n,w,l = map(int, input().split())
truck = list(map(int, input().split()))

def solv():
    now = 0
    weight = 0
    bridge = [0]*w
    answer = 0
    while True:
        if weight == 0 and now == n:
            break

        if weight != 0:
            weight = move_truce(weight,bridge)

        if now < n and weight + truck[now] <= l:
            bridge[0] = truck[now]
            weight += truck[now]
            now += 1
        answer += 1
    print(answer)
def move_truce(weight,bridge):
    if bridge[w-1] != 0:
        weight -= bridge[w-1]
        bridge[w-1] = 0
    for idx in range(w-2, -1, -1):
        bridge[idx+1], bridge[idx] = bridge[idx], 0
    return weight
solv()
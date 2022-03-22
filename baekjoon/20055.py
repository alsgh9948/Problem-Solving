from sys import stdin

input = stdin.readline

n,k = map(int, input().split())
counts = list(map(int, input().split()))
belt = [False]*(2*n)
def solv():
    zero_count = 0
    answer = 0
    while zero_count < k:
        answer += 1

        move_belt()
        zero_count += move_robot()
        zero_count += insert_robot()
    print(answer)
def insert_robot():
    global belt,counts
    if counts[0] > 0 and not belt[0]:
        counts[0] -= 1
        belt[0] = True

        if counts[0] == 0:
            return 1
    return 0

def move_robot():
    global belt,counts
    first = belt[0]
    zero_count = 0
    for idx in range(2*n-1,0,-1):
        if not belt[idx]:
            continue

        nxt = (idx+1)%(2*n)

        if counts[nxt] > 0 and not belt[nxt]:
            belt[nxt] = True
            belt[idx] = False
            counts[nxt] -= 1
            if counts[nxt] == 0:
                zero_count += 1
    if first:
        counts[1] -= 1
        if counts[1] == 0:
            zero_count += 1
        belt[1] = first
    return zero_count
def move_belt():
    global belt,counts

    belt[n-1] = False
    belt = belt[-1:]+belt[:-1]
    counts = counts[-1:]+counts[:-1]
    belt[n-1] = False

solv()
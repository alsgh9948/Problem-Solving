from sys import stdin
input = stdin.readline

data = input().strip()

def solv():
    tmp = 0
    for idx in range(0, len(data)):
        if data[idx] == '(':
            tmp += 1
        else:
            tmp -= 1

    if abs(tmp) == 0:
        print(0)
        return

    if tmp > 0:
        total = 0
        for idx in range(len(data)-1,-1,-1):
            if data[idx] == '(':
                total += 1
            else:
                total -= 1
            if total > 0:
                print(data[idx:].count('('))
                return
    else:
        total = 0
        for idx in range(0, len(data)):
            if data[idx] == '(':
                total += 1
            else:
                total -= 1
            if total < 0:
                print(data[:idx+1].count(')'))
                return
solv()
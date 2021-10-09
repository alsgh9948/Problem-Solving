from sys import stdin

input = stdin.readline

n = int(input())
before = []
for _ in range(n):
    before.append(input().strip())

after = []
for _ in range(n):
    after.append(input().strip())

def solv():
    global before
    end = n
    answer = 0
    for start in range(n):
        if before[start] != after[start]:
            answer += 1
            target = after[start]
            for idx in range(start,end):
                if before[idx] == target:
                    before = before[:start]+before[idx:idx+1]+before[start:idx]+before[idx+1:]
                    break
    print(answer)
solv()
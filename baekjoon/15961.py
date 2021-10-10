from sys import stdin

input = stdin.readline

n,d,k,c = map(int, input().split())
board = []
for _ in range(n):
    board.append(int(input()))

def solv():
    left = 0
    right = k-1

    select = [0]*(d+1)
    select[c] = 1
    total = 1
    for num in board[:k]:
        if num != c:
            if select[num] == 0:
                total += 1
            select[num] += 1
    answer = total
    while True:
        right = (right + 1)%n
        if board[right] != c:
            if select[board[right]] == 0:
                total += 1
            select[board[right]] += 1

        if board[left] != c:
            select[board[left]] -= 1
            if select[board[left]] == 0:
                total -= 1
        left = (left + 1)%n
        if left == 0:
            break
        answer = total if answer < total else answer
        if answer > k:
            break
    print(answer)
solv()
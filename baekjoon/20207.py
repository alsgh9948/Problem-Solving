from sys import stdin

input = stdin.readline

n = int(input())
board = [0]*(367)

for _ in range(n):
    s,e = map(int, input().split())
    board[s] += 1
    board[e+1] -= 1

def solv():
    max_height = 0
    length = 0
    answer = 0
    for idx in range(1,367):
        board[idx] += board[idx-1]
        if board[idx] == 0:
            answer += length * max_height
            max_height = 0
            length = 0
        else:
            max_height = board[idx] if max_height < board[idx] else max_height
            length += 1
    print(answer)

solv()
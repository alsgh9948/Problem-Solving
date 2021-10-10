from sys import stdin

input = stdin.readline
n = int(input())
board = list(map(int, input().split()))
board.sort()
answer = 9876543210
def solv():
    for out_left in range(n-3):
        for out_right in range(out_left+3,n):
            in_left = out_left+1
            in_right = out_right-1
            search(board[out_left]+board[out_right],in_left,in_right)
            if answer == 0:
                print(0)
                return
    print(answer)
def search(total,in_left,in_right):
    global answer
    while in_left < in_right:
        tmp_sum = board[in_left]+board[in_right]
        tmp = abs(total-tmp_sum)
        answer = tmp if answer > tmp else answer

        if tmp_sum > total:
            in_right -= 1
        elif tmp_sum < total:
            in_left += 1
        else:
            answer = 0
            break
solv()
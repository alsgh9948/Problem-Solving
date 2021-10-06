def solv():
    global board
    input_data = list(map(int, input().split()))
    if 6 in input_data:
        return 0
    board = []
    for idx in range(0,18,3):
        board.append(input_data[idx:idx+3])

    if go(0,1):
        return 1
    else:
        return 0

def go(now, target,):
    if target == 6:
        now += 1
        target = now + 1
    if now == 5:
        return True

    for idx in range(3):
        if board[now][idx] > 0:
            if idx == 0:
                target_idx = 2
            elif idx == 1:
                target_idx = 1
            else:
                target_idx = 0
            if board[target][target_idx] > 0:
                board[now][idx] -= 1
                board[target][target_idx] -= 1

                if go(now, target+1, ):
                    return True

                board[now][idx] += 1
                board[target][target_idx] += 1
    return False

answer = []
for _ in range(4):
    answer.append(solv())

print(*answer)
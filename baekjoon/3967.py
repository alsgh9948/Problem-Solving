from itertools import permutations
board = []
empty_point = []
alpha = [False]*13
for x in range(5):
    board.append(list(input()))
    for y in range(9):
        if board[x][y] == 'x':
            empty_point.append((x,y))
        elif 'A' <= board[x][y] <= 'L':
            board[x][y] = ord(board[x][y]) - ord('A') + 1
            alpha[board[x][y]] = True
def solv():
    target = []
    for idx in range(1,13):
        if not alpha[idx]:
            target.append(idx)

    for perm in permutations(target,len(target)):
        for idx in range(len(empty_point)):
            x,y = empty_point[idx]
            board[x][y] = perm[idx]
        if calc_sum():
            for row in board:
                for c in row:
                    if c != '.':
                        c = chr(ord('A') + c - 1)
                    print(c, end='')
                print()
            return

def calc_sum():
    sum1 = board[1][1] + board[1][3] + board[1][5] + board[1][7]
    if sum1 != 26:
        return False

    sum2 = board[3][1] + board[3][3] + board[3][5] + board[3][7]
    if sum2 != 26:
        return False

    sum3 = board[1][1] + board[2][2] + board[3][3] + board[4][4]
    if sum3 != 26:
        return False

    sum4 = board[1][7] + board[2][6] + board[3][5] + board[4][4]
    if sum4 != 26:
        return False

    sum5 = board[0][4] + board[1][3] + board[2][2] + board[3][1]
    if sum5 != 26:
        return False

    sum6 = board[0][4] + board[1][5] + board[2][6] + board[3][7]
    if sum6 != 26:
        return False

    return True


solv()
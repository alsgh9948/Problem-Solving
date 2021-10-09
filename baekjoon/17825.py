from itertools import product

dice = list(map(int, input().split()))

score = [
    [2,4,6,8,-10,12,14,16,18,-20,22,24,26,28,-30,32,34,36,38,40],
    [10,13,16,19,25,30,35,40],
    [20,22,24,25,30,35,40],
    [30,28,27,26,25,30,35,40]
]
def solv():
    for order in product([0,1,2,3],repeat=10):

def simul(order):
    board = [
        [False]*20,
        [False]*8,
        [False]*7,
        [False]*8
    ]
    h = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for idx in range(10):
        h_num = order[idx]
        dice_num = dice[idx]

        now,typ,flag = h[h_num]

        if not flag and board[now] < 0:
solv()
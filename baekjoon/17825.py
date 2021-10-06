from itertools import product

dice = list(map(int, input().split()))

score_board = [
    [-2,-4,-6,-8,-10,-12,-14,-16,-18,-20,-22,-24,-26,-28,-30,-32,-34,-36,-38,40],
    [-10,13,16,19,25,30,35,40],
    [-20,22,24,25,30,35,40],
    [-30,28,27,26,25,30,35,40]
]

real_idx_op = [0,2,3,4]
ans = 0
def solv():
    for order in product([0,1,2,3],repeat=10):
        simul(order)
    print(ans)

def simul(order):
    global ans
    h = [
        [-1, 0,-1],
        [-1, 0,-1],
        [-1, 0,-1],
        [-1, 0,-1]
    ]

    score = 0
    for idx in range(10):
        h_num = order[idx]
        dice_num = dice[idx]

        now,typ,now_score = h[h_num]
        if now == 100:
            return
        if typ == 0 and score_board[typ][now] in (-10,-20,-30):
            typ = abs(score_board[typ][now])//10
            now = 0
        nxt = now + dice_num

        if nxt >= len(score_board[typ]):
            h[h_num] = [100, typ,-1]
            continue
        nxt_score = score_board[typ][nxt]

        if check_exist(h,nxt_score):
            score += abs(nxt_score)
            h[h_num] = [nxt,typ,nxt_score]
        else:
            return
    ans = max(ans,score)


def check_exist(h,nxt_score):
    for idx in range(4):
        if h[idx][2] == nxt_score:
            return False
    return True
solv()
from itertools import product

board = [
    [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,-40],
    [0,10,13,16,19,-25,-30,-35,-40],
    [0,20,22,24,-25,-30,-35,-40],
    [0,30,28,27,26,-25,-30,-35,-40]
]

visited = [
    [0]*21,
    [0]*9,
    [0]*8,
    [0]*9
]
visited_num = 0
common = [0,0,0]
commands = list(map(int, input().split()))

answer = 0
def solv():
    for targets in product(range(4),repeat=10):
        simul(targets)
    print(answer)

def simul(targets):
    global visited, visited_num, answer
    horse_info = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    visited_num += 1
    score = 0
    for idx in range(10):
        horse_idx = targets[idx]
        typ,location,now_score = horse_info[horse_idx]

        if typ == 5:
            return

        next_typ = typ
        if typ == 0 and location in [5, 10, 15]:
            next_typ = location // 5
            next_location = 1 + commands[idx]
        else:
            next_location = location + commands[idx]

        visited[typ][location] = 0

        if next_location < len(board[next_typ]):
            next_score = board[next_typ][next_location]

            if not point_validator(next_typ,next_location,horse_info, next_score):
                return

            visited[next_typ][next_location] = visited_num

            score += abs(next_score)

            horse_info[horse_idx] = [next_typ,next_location,next_score]
        else:
            horse_info[horse_idx] = [5,0,0]

    answer = max(answer, score)

def point_validator(typ,location,horse_info,target):
    if visited[typ][location] == visited_num:
        return False
    elif target < 0:
        for typ,location,score in horse_info:
            if score < 0 and score == target:
                return False
    return True
solv()
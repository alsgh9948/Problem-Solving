from itertools import combinations
from collections import deque
tc = int(input())

def solv(t):
    global n, board, peoples, gate

    n = int(input())
    board = []
    gate = []
    peoples = []
    for x in range(n):
        board.append(list(map(int, input().split())))
        for y in range(n):
            if board[x][y] == 1:
                peoples.append((x,y))
            elif board[x][y] > 1:
                gate.append([board[x][y], (x,y)])

    set_distance()

    answer = 9876543210
    for cnt in range(len(peoples)):
        for comb in combinations(range(len(peoples)), cnt):
            gate1,gate2 = [[],[]],[[],[]]
            for idx in range(len(peoples)):
                if idx in comb:
                    gate1[0].append(-peoples[idx][0])
                    gate2[1].append(-peoples[idx][1])
                else:
                    gate2[0].append(-peoples[idx][1])
                    gate1[1].append(-peoples[idx][0])
            answer = min(answer, simul(gate1[0],gate2[0]))
            answer = min(answer, simul(gate1[1],gate2[1]))

    print('#%d %d'%(t, answer))
def simul(gate1,gate2):
    global n, board, peoples,gate
    gate1.sort()
    gate2.sort()
    t = 0
    gate1_q = deque(gate1)
    gate2_q = deque(gate2)

    while gate1_q or gate2_q:
        t += 1
        if gate1_q:
            gate1_q = check_gate_q(gate1_q,0)

        if gate2_q:
            gate2_q = check_gate_q(gate2_q,1)
    return t
def check_gate_q(gate_q,num):
    q_len = len(gate_q)
    limit = 0
    for _ in range(q_len):
        cnt = gate_q.pop()
        if cnt >= 0:
            if limit < 3:
                if cnt < gate[num][0]:
                    gate_q.appendleft(cnt+1)
                    limit += 1
            else:
                gate_q.appendleft(cnt)
        else:
            gate_q.appendleft(cnt+1)

    return gate_q
def set_distance():
    global peoples
    for idx in range(len(peoples)):
        x,y = peoples[idx]
        peoples[idx] = [distance(gate[0][1],x,y), distance(gate[1][1],x,y)]

def distance(gate,x,y):
    return abs(gate[0]-x) + abs(gate[1]-y)
for t in range(1,tc+1):
    solv(t)
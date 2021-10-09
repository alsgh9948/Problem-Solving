from sys import stdin
import math

input = stdin.readline

n,att = map(int, input().split())
board = []

for _ in range(n):
    t,a,h = map(int, input().split())
    board.append((t,a,h))
def solv():
    left = 1
    right = 123456*1000000*1000000

    while left < right:
        hp = (left+right)//2
        if simul(hp):
            right = hp
        else:
            left = hp+1
    print(right)
def simul(hp):
    at = att
    max_hp = hp
    for t,a,h in board:
        if t == 1:
            m_cnt = math.ceil(h/at)
            a_cnt = math.ceil(hp/a)
            if m_cnt <= a_cnt:
                hp -= (m_cnt-1)*a
            else:
                return False
        else:
            at += a
            hp += h
            if hp > max_hp:
                hp = max_hp
    return True

solv()
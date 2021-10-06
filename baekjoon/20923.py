from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().split())
do_deck_list = deque()
su_deck_list = deque()
tmp_do_deck,tmp_su_deck = deque(),deque()
for _ in range(n):
    a,b = map(int, input().split())
    tmp_do_deck.append(a)
    tmp_su_deck.append(b)

do_deck_list.append(tmp_do_deck)
su_deck_list.append(tmp_su_deck)
def solv():
    print(simul())
def simul():
    global do_deck_list,su_deck_list
    do_ground,su_ground = deque(),deque()
    do_deck = do_deck_list.pop()
    su_deck = su_deck_list.pop()

    typ = True
    for _ in range(m):
        if typ:
            do = do_deck.pop()
            do_ground.appendleft(do)
            if not do_deck:
                if not do_deck_list:
                    return 'su'
                else:
                    do_deck = do_deck_list.pop()
        else:
            su = su_deck.pop()
            su_ground.appendleft(su)
            if not su_deck:
                if not su_deck_list:
                    return 'do'
                else:
                    su_deck = su_deck_list.pop()
        typ = not typ
        if (do_ground and do_ground[0] == 5) or (su_ground and su_ground[0] == 5):
            if su_ground:
                do_deck_list.appendleft(su_ground)
            if do_ground:
                do_deck_list.appendleft(do_ground)
            do_ground, su_ground = deque(),deque()

        if do_ground and su_ground and do_ground[0] + su_ground[0] == 5:
            if do_ground:
                su_deck_list.appendleft(do_ground)
            if su_ground:
                su_deck_list.appendleft(su_ground)
            do_ground, su_ground = deque(), deque()


    do_score = len(do_deck)
    for deck in do_deck_list:
        do_score += len(deck)

    su_score = len(su_deck)
    for deck in su_deck_list:
        su_score += len(deck)

    if do_score > su_score:
        return 'do'
    elif do_score < su_score:
        return 'su'
    else:
        return 'dosu'

solv()
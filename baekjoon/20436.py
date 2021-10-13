ch = 'qwertyuiopasdfghjkl;zxcvbnm,./'

l,r = input().strip().split()
l = ch.index(l)
l = (l//10, l%10)
r = ch.index(r)
r = (r//10, r%10)

target = input().strip()

def solv():
    global l,r
    total = 0
    idx = 0

    while idx != len(target):
        target_idx = ch.index(target[idx])
        if target[idx] in 'qwertasdfgzxcv':
            target_idx = (target_idx//10, target_idx%10)
            total += abs(l[0]-target_idx[0])+abs(l[1]-target_idx[1])
            l = target_idx
        else:
            target_idx = ch.index(target[idx])
            target_idx = (target_idx//10, target_idx%10)
            total += abs(r[0]-target_idx[0])+abs(r[1]-target_idx[1])
            r = target_idx
        total += 1
        idx += 1
    print(total)
solv()
from sys import stdin

input = stdin.readline

def time_to_sec(t):
    t = t.split(":")
    return 60*int(t[0])+int(t[1])
s,e,q = map(time_to_sec, input().strip().split())

def solv():
    member = {}
    answer = 0
    try:
        while True:
            t,name = input().strip().split()
            t = time_to_sec(t)

            if t <= s:
                member[name] = t
            elif e <= t <= q:
                if name in member and member[name] != -1:
                    answer += 1
                    member[name] = -1
    except:
        print(answer)
solv()

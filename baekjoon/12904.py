from sys import stdin

input = stdin.readline

s = input().strip()
t = input().strip()

def solv():
    global t
    while True:
        if len(s) == len(t):
            if s == t:
                print(1)
            else:
                print(0)
            return

        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]
solv()
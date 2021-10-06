import sys
def solv():
    for y in range(1,7981):
        if e == y%15 and s == y%28 and m == y%19:
            print(y)
            return
e, s, m = map(int, sys.stdin.readline().split())

solv()

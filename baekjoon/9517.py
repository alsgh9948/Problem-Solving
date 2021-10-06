k = int(input())-1
n = int(input())

rst = []
for _ in range(n):
    a,b = input().split()
    rst.append((int(a),b))

def solv():
    global k
    t = 210
    for a,b in rst:
        t -= a
        if t <= 0:
            print(k+1)
            return
        if b == 'T':
            k = (k+1)%8
solv()
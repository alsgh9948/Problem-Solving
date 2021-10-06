from sys import stdin,stdout

input = stdin.readline
print = stdout.write
trans = lambda c : ord(c)-ord('a')
n,m = map(int, input().split())

words = []
for _ in range(n):
    word = input().strip()
    bitmask = 0
    for c in word:
        idx = trans(c)
        bitmask |= (1<<idx)
    words.append(bitmask)

def solv():
    global words
    alpha = 2**26-1

    for _ in range(m):
        op,c = input().strip().split()
        alpha_idx = trans(c)

        if op == '1':
            alpha &= ~(1<<alpha_idx)
        else:
            alpha |= (1<<alpha_idx)

        cnt = 0
        for word in words:
            if alpha & word == word:
                cnt += 1
        print('%d\n'%cnt)
solv()
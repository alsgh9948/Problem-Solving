from sys import stdin

input = stdin.readline

input_string = input().strip()

cnt = {}
for c in range(27):
    cnt[chr(ord('A')+c)] = 0

for c in input_string:
    cnt[c.upper()] += 1

cnt = sorted(cnt.items(),key=lambda x:x[1])

if len(input_string) >= 2 and cnt[-1][1] == cnt[-2][1]:
    print('?')
else:
    print(cnt[-1][0])
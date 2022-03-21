from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
time_table = defaultdict(int)
for _ in range(n):
    a,b = map(int, input().split())
    time_table[a] += 1
    time_table[b] -= 1

key_list = sorted(time_table.keys())
for idx in range(1,len(key_list)):
    time_table[key_list[idx]] += time_table[key_list[idx-1]]

max_total = sorted(time_table.items(),key=lambda x:-x[1])[0][1]

tem,txm = -1,-1
flag = False
for key in key_list:
    value = time_table[key]
    if not flag and value == max_total:
        tem = key
        flag = True
    elif flag and value != max_total:
        txm = key
        break
if txm == -1:
    txm = key_list[-1]

print(max_total)
print(tem, txm)
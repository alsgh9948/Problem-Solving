from sys import stdin

data = stdin.readline().strip()

flag = False
for idx in range(len(data)//2):
    if data[idx] != data[len(data)-1-idx]:
        print(len(data))
        break
    if data[idx] != data[idx+1]:
        flag = True
else:
    if flag:
        print(len(data)-1)
    else:
        print(-1)
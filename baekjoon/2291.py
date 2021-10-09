n = int(input())

def solv():
    end=1
    op=0
    cnt = 1
    while True:
        if n <= end:
           print(cnt)
           break
        op += 6
        end = end+op
        cnt += 1
solv()
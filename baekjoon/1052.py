n,k = map(int, input().split())

def solv():
    global n

    if bin(n).count('1') <= k:
        print(0)
    else:
        answer = 0
        while bin(n).count('1') > k:
            cnt = 2**bin(n)[::-1].index('1')
            n += cnt
            answer += cnt
        print(answer)
solv()
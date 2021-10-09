d,k = map(int, input().split())

def solv():
    for num in range(k-1,0,-1):
        a = k
        b = num
        cnt = 1
        while True:
            if cnt == d-1:
                print(b)
                print(a)
                return
            a,b = b,a-b
            cnt += 1
            if a < b:
                break
solv()
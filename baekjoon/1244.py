n = int(input())
switch = list(map(int, input().split()))

m = int(input())

def solv():
    global switch
    for _ in range(m):
        gender, target = map(int, input().split())
        if gender == 1:
            for idx in range(target-1,n,target):
                switch[idx] ^= 1
        else:
            l=r=target-1
            flag = False
            for _ in range(min(target-1,n-target)):
                l -= 1
                r += 1
                if switch[l] != switch[r]:
                    for idx in range(l+1,r):
                        switch[idx] ^= 1
                    flag = True
                    break
            if not flag and (l == 0 or r == n-1 or switch[l-1] != switch[r+1]):
                for idx in range(l,r+1):
                    switch[idx] ^= 1
    for idx in range(0,n,20):
        print(*switch[idx:idx+20])
solv()
c, p = map(int,input().strip().split())

h = list(map(int, input().strip().split()))

ans = 0
for i in range(c):
    if p == 1:
        ans += 1
        if i+3 < c and h[i] == h[i+1] == h[i+2] == h[i+3]:
            ans += 1
    elif p == 2:
        if i+1 < c and h[i] == h[i+1]:
            ans += 1
    elif p == 3:
        if i+2 < c:
            if h[i] == h[i+1] and h[i]+1 == h[i+2]:
                ans += 1
        if i+1 < c:
            if h[i]-1 == h[i+1]:
                ans += 1
    elif p == 4:
        if i+2 < c:
            if h[i]-1 == h[i+1] and h[i+1] == h[i+2]:
                ans += 1
        if i+1 < c:
            if h[i]+1 == h[i+1]:
                ans += 1
    elif p == 5:
        if i+2 < c:
            if h[i] == h[i+1] == h[i+2]:
                ans += 1
            if h[i] == h[i+2] and h[i]-1 == h[i+1]:
                ans += 1
        if i+1 < c:
            if h[i]-1 == h[i+1]:
                ans += 1
            if h[i]+1 == h[i+1]:
                ans += 1
    elif p == 6:
        if i+2 < c:
            if h[i] == h[i+1] == h[i+2]:
                ans += 1
            if h[i]+1 == h[i+1] and h[i+1] == h[i+2]:
                ans += 1
        if i+1 < c:
            if h[i]-2 == h[i+1]:
                ans += 1
            if h[i] == h[i+1]:
                ans += 1
    elif p == 7:
        if i+2 < c:
            if h[i] == h[i+1] == h[i+2]:
                ans += 1
            if h[i] == h[i+1] and h[i+1]-1 == h[i+2]:
                ans += 1
        if i+1 < c:
            if h[i]+2 == h[i+1]:
                ans += 1
            if h[i] == h[i+1]:
                ans += 1

print(ans)
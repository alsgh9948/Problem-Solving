tc = int(input())

def solv():
    word = input().strip()
    used = [False]*26

    before = ''
    for c in word:
        if before != c:
            if not used[ord(c)-ord('a')]:
                used[ord(c) - ord('a')] = True
                before = c
            else:
                return False
    return True

answer = 0
for _ in range(tc):
    if solv():
        answer += 1
print(answer)
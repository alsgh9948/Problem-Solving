from sys import stdin

def trans_char_to_int(c):
    return ord(c)-ord('a')

def word_check():
    cnt = 0
    for word in word_list:
        flag = True
        for c in word:
            idx = trans_char_to_int(c)
            if not select_alpha_check[idx]:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt

def select_alpha(cnt, start):
    if cnt == k-5:
        global ans
        ans = max(ans, word_check())
        return

    for i in range(start, len(alpha_list)):
        idx = trans_char_to_int(alpha_list[i])
        if not select_alpha_check[idx]:
            select_alpha_check[idx] = True
            select_alpha(cnt+1, i+1)
            select_alpha_check[idx] = False


def solv():
    global n,k,word_list,select_alpha_check,alpha_list,ans

    ans = 0
    n, k = map(int, stdin.readline().strip().split())

    word_list = []
    select_alpha_check = [False]*26
    alpha_list = ['a','n','t','i','c']

    select_alpha_check[ord('a') - ord('a')] = True
    select_alpha_check[ord('n') - ord('a')] = True
    select_alpha_check[ord('t') - ord('a')] = True
    select_alpha_check[ord('i') - ord('a')] = True
    select_alpha_check[ord('c') - ord('a')] = True

    for _ in range(n):
        word = stdin.readline().strip()
        word_list.append(word)
        for c in word:
            idx = trans_char_to_int(c)
            if not c in alpha_list:
                alpha_list.append(c)

    if k < 5:
        print(0)
    elif k >= len(alpha_list):
        print(n)
    else:
        select_alpha(0,5)
        print(ans)
solv()
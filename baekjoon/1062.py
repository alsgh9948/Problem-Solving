from sys import stdin

n,k = map(int,stdin.readline().strip().split())

word_list = []
alpha = [False]*26
select_list = [False]*26
alpha_list = []
ans = 0

def convert_char_to_int(c):
    return ord(c)-ord('a')

select_list[convert_char_to_int('a')] = alpha[convert_char_to_int('a')] = True
select_list[convert_char_to_int('n')] = alpha[convert_char_to_int('n')] = True
select_list[convert_char_to_int('t')] = alpha[convert_char_to_int('t')] = True
select_list[convert_char_to_int('i')] = alpha[convert_char_to_int('i')] = True
select_list[convert_char_to_int('c')] = alpha[convert_char_to_int('c')] = True

for _ in range(n):
    word = stdin.readline().strip()
    word_list.append(word)
    for c in word:
        idx = convert_char_to_int(c)
        if not alpha[idx]:
            alpha[idx] = True
            alpha_list.append(c)

def select_alpha(cnt, idx, select_list):
    global ans
    if cnt == k-5:
        ans = max(ans, check_word(select_list))
        return

    for i in range(idx, len(alpha_list)):
        alpha_idx = convert_char_to_int(alpha_list[i])
        select_list[alpha_idx] = True
        select_alpha(cnt+1,i+1,select_list)
        select_list[alpha_idx] = False


def check_word(select_list):
    cnt = 0
    for word in word_list:
        flag = True
        for c in word[4:-4]:
            idx = convert_char_to_int(c)
            if not select_list[idx]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt


select_alpha(0,0,select_list)
print(ans)
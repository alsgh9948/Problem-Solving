start = input()
def calc_next_num(n):
    tmp = n.ljust(2,'0')
    tmp = str(int(tmp[0])+int(tmp[1]))[-1]

    return n[-1]+tmp

now = start
nxt = calc_next_num(now)
answer = 1
while int(start) != int(nxt):
    nxt = calc_next_num(nxt)
    answer += 1
print(answer)
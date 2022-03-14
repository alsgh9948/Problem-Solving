cash = int(input())
stock = list(map(int, input().split()))

def solv():
    j = bnp()
    s = timing()
    jtotal = j[0]+j[1]*stock[-1]
    stotal = s[0]+s[1]*stock[-1]
    if jtotal == stotal:
        print("SAMESAME")
    elif jtotal > stotal:
        print("BNP")
    else:
        print("TIMING")

def timing():
    now = cash
    count = 0
    yesterday = stock[0]
    typ = 0
    tmp = 0
    for price in stock[1:]:
        if price > yesterday:
            if typ != 1:
                typ = 1
                tmp = 1
            else:
                tmp += 1
                if tmp >= 3:
                    now += price*count
                    count = 0
        elif price < yesterday:
            if typ != -1:
                typ = -1
                tmp = 1
            else:
                tmp += 1
                if tmp >= 3:
                    count += now//price
                    now = now % price
        yesterday = price

    return now, count
def bnp():
    now = cash
    count = 0
    for price in stock:
        if now >= price:
            count += now//price
            now = now%price

    return now, count
solv()
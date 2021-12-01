from sys import stdin

input = stdin.readline

ip = input().strip()

def solv():
    global ip
    ip = ip.split(":")

    after_ip = ''
    if len(ip) == 3:
        if not ip[0] and not ip[-1]:
            after_ip = ('0000:'*8)[:-1]
        elif ip[0] and ip[-1]:
            after_ip = ip[0].zfill(4) + ':0000' * 6 + ':'+ip[-1].zfill(4)
        elif ip[0]:
            after_ip = ip[0].zfill(4) + ':0000'*7
        elif ip[-1]:
            after_ip = '0000:'*7 + ip[-1].zfill(4)
        print(after_ip)
    else:
        if len(ip) == 9:
            if not ip[0]:
                ip = ip[1:]
            else:
                ip = ip[:-1]
        for group in ip:
            if group:
                after_ip += group.zfill(4)+':'
            else:
                after_ip += 'target:'
        after_ip = after_ip.replace('target:','0000:'*(8-len(ip)+1))
        print(after_ip[:-1])

solv()
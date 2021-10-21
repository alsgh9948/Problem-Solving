n = int(input())
MAX = int(n**(1/2))+1
def solv():
    flag = [False,False,False,False]
    for a in range(1,MAX):
        tmp1 = a*a
        if tmp1 == n:
            print(1)
            return
        elif not flag[1]:
            for b in range(1,MAX):
                tmp2 = tmp1+b*b
                if tmp2 == n:
                    flag[1] = True
                    break
                elif tmp2 > n:
                    break
                elif flag[2]:
                    continue
                else:
                    for c in range(1,MAX):
                        tmp3 = tmp2+c*c
                        if tmp3 == n:
                            flag[2] = True
                            break
                        elif tmp3 > n:
                            break
                        elif flag[3]:
                            continue
                        else:
                            for d in range(1,MAX):
                                tmp4 = tmp3+d*d
                                if tmp4 == n:
                                    flag[3] = True
                                    break
                                elif tmp4 > n:
                                    break
    print(flag.index(True)+1)
solv()
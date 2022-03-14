from sys import stdin

input = stdin.readline

a,b,c,x,y = map(int, input().split())

def solv():
    if c*2 < a+b:
        result = min(x,y)*c*2
        if x < y:
            if b > c*2:
                return result + (y-x)*2*c
            else:
                return result + (y-x)*b
        else:
            if a > c*2:
                return result + (x-y)*2*c
            else:
                return result + (x-y)*a

    else:
        return a*x+b*y

print(solv())